#!/usr/bin/env bash

IP=$(cat $1)
PASS="${AUTOBASHPASS}"

for con in $IP; do
  echo $con
  echo $PASS | sshpass -p"$PASS" -v ssh -o "StrictHostKeyChecking no" -t $con "sudo -S apt-get -y install php7.4-cli"
done;
