#!/bin/bash

# Echo usage if something isn't right.
usage() {
    echo "Usage: $0 [-p <80|443>] [-h <string>] [-f]" 1>&2; exit 1;
}

while getopts ":p:h:f" o; do
    case "${o}" in
        p)
            PORT=${OPTARG}
            [[ $PORT != "80" && $PORT != "443" ]] && usage
            ;;
        h)
            HOST=${OPTARG}
            ;;
        f)
            FORCE=1
            ;;
        :)
            echo "ERROR: Option -$OPTARG requires an argument"
            usage
            ;;
        \?)
            echo "ERROR: Invalid option -$OPTARG"
            usage
            ;;
    esac
done
shift $((OPTIND-1))

# Check required switches exist
if [ -z "${PORT}" ] || [ -z "${HOST}" ]; then
    usage
fi

echo "p = ${PORT}"
echo "h = ${HOST}"
