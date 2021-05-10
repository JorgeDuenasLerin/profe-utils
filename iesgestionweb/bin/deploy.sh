#!/bin/bash

if [ -z "$1" ]
  then
    echo "No secret.json"
  exit
fi

su -

git pull


DST_PATH="/var/www/iesgestionweb/"



echo "Copying files to /var/"

cp manage.py $DST_PATH
cp -r iesgestionweb/ $DST_PATH
cp -r incidencias/ $DST_PATH
