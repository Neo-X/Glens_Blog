#!/bin/bash

make publish
cp -r output/* /var/www/html/
cp -r content/projects/* /var/www/html/projects/
