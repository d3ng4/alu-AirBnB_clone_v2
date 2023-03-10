#!/usr/bin/python3
"""
script that deletes out-of-date archives,
using the function do_clean
"""
from fabric.api import local
from fabric.api import env
env.hosts = ['107.23.168.84', '52.90.109.65']  # list of web servers


def do_clean(number=0):
    """
    function that deletes out-of-date archives
    """
    number = int(number)
    if number == 0 or number == 1:
        local("ls -t versions | tail -n +2 | xargs rm -f")
    else:
        local("ls -t versions | tail -n +{} | xargs rm -f".format(number + 1))
    # local("ls -t versions | tail -n +2 | xargs rm -f") # delete all but last
    # local("ls -t versions | tail -n +3 | xargs rm -f") # delete all but last 2
    # local("ls -t versions | tail -n +4 | xargs rm -f") # delete all but last
    # 3
