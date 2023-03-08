#!/usr/bin/python3
"""
script that distributes an archive to your web servers,
using the function do_deploy
"""

def do_deploy(archive_path):
    """
    function that distributes an archive to web servers
    """
    import os
    from fabric.api import put, run, env
    env.hosts = ['ip_web-01', 'ip_web-02'] # list of web servers
    if archive_path is None or not os.path.exists(archive_path): 
        return False
    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # create a folder with the same name as the archive
        # without the extension
        run("mkdir -p /data/web_static/releases/{}".format(archive_path))
        # uncompress the archive to the folder
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(archive_path))
        # delete the archive from the web server
        run("rm /tmp/{}.tgz".format(archive_path))
        # delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # create a new the symbolic link /data/web_static/current on the web server,
        # linked to the new version of your code
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(archive_path))
        return True
    except:
        return False

