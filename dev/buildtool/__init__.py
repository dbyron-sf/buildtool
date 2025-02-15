"""Support for spinnaker releases."""

# pylint: disable=wrong-import-position

# These would be required if running from source code
SPINNAKER_RUNNABLE_REPOSITORY_NAMES = [
    "clouddriver",
    "deck",
    "echo",
    "fiat",
    "front50",
    "gate",
    "igor",
    "kayenta",
    "orca",
    "rosco",
]
# These are not included in the BOM but are included in some buildtool tasks
SPINNAKER_RUNNABLE_NON_CORE_REPOSITORY_NAMES = ["keel"]

# Imported by runnable services
SPINNAKER_LIBRARY_REPOSITORY_NAMES = ["kork"]

# For building and validating a release
SPINNAKER_PROCESS_REPOSITORY_NAMES = ["buildtool", "spinrel"]

# Additional tools that accompany a release
SPIN_REPOSITORY_NAMES = ["spin"]

# Halyard is independent of spinnaker
SPINNAKER_HALYARD_REPOSITORY_NAME = "halyard"

# Documentation is version agnostic
SPINNAKER_IO_REPOSITORY_NAME = "spinnaker.io"
SPINNAKER_CHANGELOG_BASE_URL = "https://spinnaker.io/changelogs"  # /M.m.p-changelog/

# Artifact sources are per GitHub Action build jobs
SPINNAKER_DEBIAN_REPOSITORY = "https://us-apt.pkg.dev/projects/spinnaker-community"
SPINNAKER_DOCKER_REGISTRY = "us-docker.pkg.dev/spinnaker-community/docker"
SPINNAKER_GOOGLE_IMAGE_PROJECT = "marketplace-spinnaker-release"
SPINNAKER_HALYARD_GCS_BUCKET_NAME = "halconfig"


from buildtool.util import (
    DEFAULT_BUILD_NUMBER,
    add_parser_argument,
    unused_port,
    log_timestring,
    timedelta_string,
    log_embedded_output,
    ensure_dir_exists,
    write_to_path,
)

from buildtool.errors import (
    BuildtoolError,
    ConfigError,
    ExecutionError,
    ResponseError,
    TimeoutError,
    UnexpectedError,
    exception_to_message,
    maybe_log_exception,
    raise_and_log_error,
    check_kwargs_empty,
    check_options_set,
    check_path_exists,
    # This is very specialized, but here to share
    # between validate_bom__deploy and image_commands
    scan_logs_for_install_errors,
)

from buildtool.subprocess_support import (
    start_subprocess,
    wait_subprocess,
    run_subprocess,
    check_subprocess,
    check_subprocess_sequence,
    run_subprocess_sequence,
    check_subprocesses_to_logfile,
    determine_subprocess_outcome_labels,
)

from buildtool.git_support import (
    GitRepositorySpec,
    GitRunner,
    CommitMessage,
    CommitTag,
    RepositorySummary,
    SemanticVersion,
)

from buildtool.hal_support import HalRunner

from buildtool.scm import SourceInfo, SpinnakerSourceCodeManager

from buildtool.bom_scm import SPINNAKER_BOM_REPOSITORY_NAMES, BomSourceCodeManager

from buildtool.branch_scm import BranchSourceCodeManager

from buildtool.command import CommandFactory, CommandProcessor

from buildtool.repository_command import (
    RepositoryCommandProcessor,
    RepositoryCommandFactory,
)

from buildtool.gradle_support import (
    GradleCommandFactory,
    GradleCommandProcessor,
    GradleRunner,
)

from buildtool.metrics import MetricsManager
