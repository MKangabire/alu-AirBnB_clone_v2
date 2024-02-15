#!/usr/bin/python3
"""decompresses and compresses"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_{0}.tgz".format(timestamp)
    archive_path = "versions/{0}".format(archive_name)

    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Compress the contents of the web_static folder into a .tgz archive
    result = local("tar -cvzf {archive_path} web_static".format(archive_path))

    # Check if the archive was generated successfully
    if result.failed:
        return None
    else:
        return archive_path

