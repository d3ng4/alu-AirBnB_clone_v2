#!/usr/bin/python3
"""
script that creates and distributes an archive to your web servers,
using the function deploy
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

def deploy():
    """
    function that creates and distributes an archive to web servers
    """
    from fabric.api import env
    env.hosts = ['ip_web-01', 'ip_web-02']  # list of web servers
    archive_path = do_pack() 
    if archive_path is None:  # if archive_path is None:
        return False
    return do_deploy(archive_path)  # deploy = do_pack() + do_deploy()