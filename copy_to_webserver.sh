#!/bin/bash

./buildAndDeploy.sh
rsync -av -e ssh /var/www/html/~gberseth/* gberseth@arcade.iro.umontreal.ca:/home/www-labs/gberseth/public_html/
# rsync -av -e ssh content/projects/* gberseth@ftp.fracturedplane.com:~/public_html/projects
