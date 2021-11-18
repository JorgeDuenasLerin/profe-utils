#!/usr/bin/env bash

IP=$(cat $1)
PASS="${AUTOBASHPASS}"
FILE=$2

# Ejem: "apt-get -y install php7.4-cli"

for con in $IP; do
  echo $con
  echo $PASS | sshpass -p"$PASS" -v scp -v -o "StrictHostKeyChecking no" $FILE $con:/home/administrador/
done;
