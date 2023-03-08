#!/usr/bin/python3
"""
script that deletes out-of-date archives,
using the function do_clean
"""


def do_clean(number=0):
    """
    function that deletes out-of-date archives
    """
    from fabric.api import local
    from fabric.api import env
    env.hosts = ['ip_web-01', 'ip_web-02']  # list of web servers
    number = int(number)
    if number == 0 or number == 1:
        local("ls -t versions | tail -n +2 | xargs rm -f")
    else:
        local("ls -t versions | tail -n +{} | xargs rm -f".format(number + 1))
    # local("ls -t versions | tail -n +2 | xargs rm -f") # delete all but last
    # local("ls -t versions | tail -n +3 | xargs rm -f") # delete all but last 2
    # local("ls -t versions | tail -n +4 | xargs rm -f") # delete all but last
    # 3
