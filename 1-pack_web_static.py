#!/usr/bin/python3
"""
creating a .tgz archive from contents of web_static
folder using do_pack.
"""


def do_pack():
    """create folder versions if it doesnt exist
    and pack files of web_static """
    from datetime import datetime
    from fabric.api import local
    import os
    path = "versions"
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    command = "tar -cvzf versions/web_static_{}.tgz web_static".format(date)
    local(command)  # local("mkdir -p versions")
    new_file_name = "web_static_{}.tgz".format(date)
    # print("New file created: {}".format(new_file_name))
    # local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
    # command = "tar -carvf web_static alu-AirBnB_clone_v2"
    archive_path = "{}/{}".format(path, new_file_name)
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None

# x = do_pack()
# print(x)
