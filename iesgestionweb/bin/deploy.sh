#!/bin/bash

if [ -z "$1" ]
  then
    echo "No secret.json"
  exit
fi
"""

source
collectstatic

"""
secrets=$1

git pull

DST_PATH="/var/www/iesgestionweb/"

echo "Copying files to $DST_PATH"
rm -r $DST_PATH
mkdir -p $DST_PATH

cp $secrets $DST_PATH
cp manage.py $DST_PATH
cp -r iesgestionweb/ $DST_PATH
cp -r incidencias/ $DST_PATH
cp -r static/ $DST_PATH

chown -R www-data:www-data $DST_PATH
