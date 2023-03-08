#!/usr/bin/python3
"""
creating a .tgz archive from contents of web_static
folder using do_pack.
"""

def do_pack():
  """create folder versions if it doesnt exist
  and pack files of web_static """
  
  tar -carvf web_static alu-AirBnB_clone_v2
