#!/bin/bash

make publish
rsync -av -e ssh gberseth@login.eecs.berkeley.edu:~/public_html/ /var/www/html
