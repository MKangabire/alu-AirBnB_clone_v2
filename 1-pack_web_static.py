#!/usr/bin/python3
from fabric import task
from fabric.context_managers import cd
from fabric.operations import local
from datetime import datetime

@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'
    archive_path = f'versions/{archive_name}'

    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Compress the contents of the web_static folder into a .tgz archive
    result = local(f'tar -cvzf {archive_path} web_static')

    # Check if the archive was generated successfully
    if result.failed:
        return None
    else:
        return archive_path

