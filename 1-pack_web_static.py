#!/usr/bin/python3
"""
module - creating a .tgz archive from contents of web_static
folder using do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    create folder versions if it doesnt exist
    and pack files of web_static
    """

    try:
        path = "versions"
        # if not os.path.exists(path):
        #     os.makedirs(path)
        #  or
        if os.path.isdir(path) is False:
            local("mkdir versions")  # create folder versions
        now = datetime.now()
        date = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        command = f"tar -cvzf {file_name} web_static"
        local(command)
        return file_name
    except BaseException:
        return None

# x = do_pack()
# print(x)
