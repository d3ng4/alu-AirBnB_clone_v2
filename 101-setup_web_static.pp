# using puppet to install and configure a web server
# install nginx if not already installed
package {'nginx':
         ensure = > 'installed',
         provider = > 'apt',
         }

# start nginx if not already running
service {'nginx':
         ensure = > 'running',
         enable = > true,
         }

# create folder /data/web_static
file {'/data/web_static':
      ensure = > 'directory',
      }
# create folder /data/web_static/releases
file {'/data/web_static/releases':
      ensure = > 'directory',
      }
# create folder /data/web_static/releases/test
file {'/data/web_static/releases/test':
      ensure = > 'directory',
      }
# create folder /data/web_static/shared
file {'/data/web_static/shared':
      ensure = > 'directory',
      }
# create folder /data/web_static/shared/test
file {'/data/web_static/shared/test':
      ensure = > 'directory',
      }
# create file /data/web_static/releases/test/index.html
file {'/data/web_static/releases/test/index.html':
      ensure = > 'file',
      content = > 'Holberton School',
      }
# delete symbolic link /data/web_static/current
file {'/data/web_static/current':
      ensure = > 'absent',
      }
# create symbolic link /data/web_static/current
file {'/data/web_static/current':
      ensure = > 'link',
      target = > '/data/web_static/releases/test',
      }
# give ownership of /data/ to www-data
file {'/data/':
      ensure = > 'directory',
      owner = > 'ubuntu',
      group = > 'ubuntu',
      mode = > '0755',
      }
# add nginx config
file {'/etc/nginx/sites-available/default':
      ensure = > 'file',
      content = > template('web_static/'),
      notify = > Service['nginx'],
      }
# restart nginx
service {'nginx':
         ensure = > 'running',
         enable = > true,
         }
