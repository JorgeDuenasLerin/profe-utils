#!/bin/bash

if [ -z "$1" ]
  then
    echo "No secret.json"
  exit
fi

secrets=$1

git pull

DST_PATH="/var/www/iesgestionweb/"

echo "Copying files to $DST_PATH"
mkdir -p $DST_PATH

cp $secrets $DST_PATH
cp manage.py $DST_PATH
cp -r iesgestionweb/ $DST_PATH
cp -r incidencias/ $DST_PATH

chmod -r www-data:www-data $DST_PATH
