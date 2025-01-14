from haupt.common.apis.regex import (
    OWNER_NAME_PATTERN,
    PROJECT_NAME_PATTERN,
    UUID_PATTERN,
)

# Projects
URLS_PROJECTS_CREATE = r"^{}/projects/create/?$".format(OWNER_NAME_PATTERN)
URLS_PROJECTS_LIST = r"^{}/projects/list/?$".format(OWNER_NAME_PATTERN)
URLS_PROJECTS_NAMES = r"^{}/projects/names/?$".format(OWNER_NAME_PATTERN)
URLS_PROJECTS_DETAILS = r"^{}/{}/?$".format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN)

# Resources
URLS_PROJECTS_RUNS_TAG = r"^{}/{}/runs/tag/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_STOP = r"^{}/{}/runs/stop/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_APPROVE = r"^{}/{}/runs/approve/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_DELETE = r"^{}/{}/runs/delete/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_SYNC = r"^{}/{}/runs/sync/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_ARTIFACTS_LINEAGE_V0 = r"^{}/{}/runs/artifacts_lineage/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_ARTIFACTS_LINEAGE = r"^{}/{}/runs/lineage/artifacts/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_LIST = r"^{}/{}/runs/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)

URLS_PROJECTS_ARCHIVE = r"^{}/{}/archive/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RESTORE = r"^{}/{}/restore/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_BOOKMARK = r"^{}/{}/bookmark/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_UNBOOKMARK = r"^{}/{}/unbookmark/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)

URLS_PROJECTS_RUNS_INVALIDATE = r"^{}/{}/runs/invalidate/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_BOOKMARK = r"^{}/{}/runs/bookmark/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_ACTIVITIES = r"^{}/{}/activities/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)

URLS_PROJECTS_ARTIFACT_UPLOAD = r"^{}/{}/artifacts/{}/upload?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, UUID_PATTERN
)
URLS_PROJECTS_RUNS_TRANSFER = r"^{}/{}/runs/transfer/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_ARCHIVE = r"^{}/{}/runs/archive/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_RUNS_RESTORE = r"^{}/{}/runs/restore/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECTS_STATS = r"^{}/{}/stats/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
