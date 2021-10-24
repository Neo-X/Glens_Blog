#!/bin/bash

make publish
cp -r output/* /var/www/html/~gberseth/
cp -r content/projects/* /var/www/html/~gberseth/projects/
