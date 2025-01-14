import os

import typer
from dotenv import load_dotenv

from lupin_grognard.__init__ import __version__
from lupin_grognard.core.check import check_commit, check_max_allowed_major_commits
from lupin_grognard.core.commit.commit import Commit
from lupin_grognard.core.commit.commit_validator import (
    define_commits_check_mode,
    CommitCheckModes,
)
from lupin_grognard.core.config import MAIN_BRANCHES_LIST
from lupin_grognard.core.doc_generator.changelog import Changelog
from lupin_grognard.core.doc_generator.reviewlog import Reviewlog
from lupin_grognard.core.doc_generator.ros2_docs import Ros2Docs
from lupin_grognard.core.format.clang_format import ClangFormatter
from lupin_grognard.core.format.cmake_format import CMakeFormatter
from lupin_grognard.core.git import Git
from lupin_grognard.core.gitlab import get_ci_mr_target_branch
from lupin_grognard.core.tools.ros2.package import find_ros_packages

from .core.tools.log_utils import die, info, warn
from .core.tools.utils import (
    configure_logging,
    display_number_of_commits_to_check,
    display_supported_commit_types,
    generate_commit_list,
    generate_commits_range_to_check,
    get_current_branch_name,
)

load_dotenv()
GROG_BRANCHES = os.getenv("GROG_BRANCHES")
GROG_MAX_ALLOWED_COMMITS = os.getenv("GROG_MAX_ALLOWED_COMMITS")
GROG_DONT_CHECK_FOR_APPROVERS = os.getenv("GROG_DONT_CHECK_FOR_APPROVERS")
GROG_CLANG_FORMAT = os.getenv("GROG_CLANG_FORMAT")


cli = typer.Typer()


@cli.command()
def version():
    print(f"Version: {__version__}")


@cli.command()
def check_commits(
    CHECK_ALL_COMMITS: bool = typer.Option(
        False, "--all", "-a", help="check all commits from initial commit"
    ),
    grog_max_allowed_commits: int = typer.Option(
        1, "--grog-max-allowed-commits", "-max", envvar="GROG_MAX_ALLOWED_COMMITS"
    ),
    permissive_mode: bool = typer.Option(
        False, "--permissive", "-p", help="ignore command failure"
    ),
    no_jama: bool = typer.Option(False, "--no-jama", "-nj", help="ignore jama check"),
    no_approvers: bool = typer.Option(
        False, "--no-approvers", "-na", help="ignore approver check"
    ),
):
    """
    Supported commit types: build(add|change|remove), bump, ci, deps(add|change|remove), docs, enabler,
    feat(add|change|remove), fix, refactor, test.
    Only one major commit types allowed per branch: "enabler", "feat", "fix" or "refactor".

    Check every commit message since the last "merge request" in any of the branches in the
    main_branches_list : "main", "master", "dev", "develop", "development"

    - With --all option :
    grog check-commits [--all or -a] to check all commits from initial commit.
    This option is automatically set if current branch is a main one.

    - With --grog-max-allowed-commits option :
    grog check-commits [--grog-max-allowed-commits or -max] {int} to set the maximum number
    of commits allowed to the branch.
    Example : grog check-commits --grog-max-allowed-commits 10

    - With --permissive option :
    grog check-commits [--permissive or -p] to ignore command failure.
    This option is ignored for the 'main' and 'master' branches.

    - With --no-jama option :
    grog check-commits [--no-jama or -nj] to ignore jama check.

    - With --no-approvers option :
    grog check-commits [--no-approvers or -na] to ignore approver check.

    You can set GROG_MAX_ALLOWED_COMMITS env var in .env, .gitlab-ci.yml, gitlab...
    """
    configure_logging()
    git = Git()
    git.ensure_valid_git_repository()

    current_branch_name = get_current_branch_name()
    ci_mr_target_branch_name = get_ci_mr_target_branch()

    check_mode = define_commits_check_mode(
        current_branch=current_branch_name,
        ci_mr_target_branch=ci_mr_target_branch_name,
        CHECK_ALL_COMMITS_flag=CHECK_ALL_COMMITS,
    )

    if CHECK_ALL_COMMITS:
        info(msg="Processing all commits since initial commit as '--all' option is set")
    if no_jama:
        warn(msg="JAMA item referencing check disabled as '--no-jama' option is set")
    if no_approvers:
        warn(msg="Approver check disabled as '--no-approvers' option is set")

    if check_mode == CommitCheckModes.CHECK_ALL_COMMITS:
        grog_max_allowed_commits = 0
        git_log = git.get_log()
        commits = generate_commit_list(git_log.stdout)

        if ci_mr_target_branch_name in MAIN_BRANCHES_LIST:
            info(
                msg=(
                    "Processing check-commits for a pipeline merge request result "
                    f"to a '{ci_mr_target_branch_name}' target branch"
                )
            )
            commits = generate_commits_range_to_check(
                branch_list=MAIN_BRANCHES_LIST,
                commits=commits,
                ci_mr_target_branch_name=ci_mr_target_branch_name,
            )

    elif check_mode == CommitCheckModes.CHECK_CURRENT_BRANCH_ONLY:
        git_log = git.get_log(max_line_count=50, first_parent=True)
        commits = generate_commit_list(git_log.stdout)
        commits = generate_commits_range_to_check(
            branch_list=MAIN_BRANCHES_LIST,
            commits=commits,
        )

    if check_max_allowed_major_commits(
        commits=commits,
        major_commit_limit=grog_max_allowed_commits,
    ):
        display_supported_commit_types()
        display_number_of_commits_to_check(commits=commits)
        check_commit(
            commits=commits,
            check_mode=check_mode,
            permissive_mode=permissive_mode,
            no_jama=no_jama,
            no_approvers=no_approvers,
        )


@cli.command()
def format(
    clang_format: str = typer.Option(
        "clang-format-14", "--clang-format", "-cf", envvar="GROG_CLANG_FORMAT"
    )
):
    """Format C/C++ files with clang-format
    You can set GROG_CLANG_FORMAT env var in order to configure the executable to be used
    """
    configure_logging()
    clang_formater = ClangFormatter(name=clang_format)
    clang_formater.format_c_cpp_files()

    cmake_formater = CMakeFormatter()
    cmake_formater.format_cmake_files()


@cli.command()
def changelog():
    """Generate changelog"""
    configure_logging()
    git = Git()
    git.ensure_valid_git_repository()
    git_log = git.get_log()
    if git_log.stderr:
        die(f"git error {git_log.return_code}, {git_log.stderr}")
    commits = generate_commit_list(commits_string=git_log.stdout)
    commits = Commit.add_additional_commit_info(commits=commits)
    Changelog(commits=commits).generate()


@cli.command()
def reviewlog():
    """Generate REVIEWLOG.html"""
    configure_logging()
    git = Git()
    git.ensure_valid_git_repository()
    git_log = git.get_log()
    if git_log.stderr:
        die(f"git error {git_log.return_code}, {git_log.stderr}")
    commits = generate_commit_list(commits_string=git_log.stdout)
    commits = Commit.add_additional_commit_info(commits=commits)
    Reviewlog(commits=commits).generate()


@cli.command()
def ros2docs(
    path: str = typer.Option(
        ..., "--path", "-p", help="path to search for ROS2 packages"
    )
):
    """Generate ROS2 documentation"""
    configure_logging()

    ros_packages = find_ros_packages(path)
    for path in ros_packages:
        api_doc = Ros2Docs(path=path)
        api_doc.generate_api_docs()
