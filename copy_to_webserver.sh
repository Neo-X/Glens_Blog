#!/bin/bash

./buildAndDeploy.sh
# rsync -av -e ssh /var/www/html/* gberseth@arcade.iro.umontreal.ca:/home/www-labs/gberseth/public_html/
## Use filezilla
# rsync -av -e ssh content/projects/* gberseth@ftpes.fracturedplane.com:~/public_html/projects
