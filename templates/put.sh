#!/bin/bash
if [ -z "$1" ] || [ ! -f "$1" ]; then
  echo ERROR. Specify template file name as parameter
  exit 1
fi

TEMPLATE_FILE=$1
TEMPLATE_NAME=$(echo $TEMPLATE_FILE | sed 's|.json||')

curl -X PUT -H 'Content-Type: application/json' -d@${TEMPLATE_NAME}.json 127.0.0.1:9200/_template/$TEMPLATE_NAME 
echo