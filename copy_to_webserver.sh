#!/bin/bash

make publish
rsync -av -e ssh output/* gberseth@ftp.fracturedplane.com:~/
rsync -av -e ssh content/projects/* gberseth@ftp.fracturedplane.com:~/public_html/projects
