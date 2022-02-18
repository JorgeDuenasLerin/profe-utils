#!/usr/bin/env bash

IP=$(cat $1)
PASS="${AUTOBASHPASS}"
CMD=$2

# Ejem: "apt-get -y install php7.4-cli"

for con in $IP; do
  echo $con
  echo $PASS | sshpass -p"$PASS" -v ssh -o "StrictHostKeyChecking no" -t $con "sudo -S $CMD"
done;
