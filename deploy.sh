#!/bin/bash
function generate_post_data() {
    cat <<EOF
{
    "version": "${1}",
    "description": "${@:2}",
    "timestamp": "$(date +%Y-%m-%dT%H:%M:%S%:z)"
}
EOF
}

if [ -z "${1}" ]; then
  echo ERROR. specify app version
  exit 1
fi

if [ -z "${2}" ]; then
  echo ERROR. specify description
  exit 1
fi

docker build -t petshop petshop
docker rmi $(docker images -q -f dangling=true) || true

APP_VER=$1 docker-compose -f docker-compose.yaml -f docker-compose.petshop.yaml up -d


curl -X POST -H 'Content-Type: application/json' 127.0.0.1:9200/deployments/_doc  -d@<(generate_post_data ${1} ${@:2})
echo