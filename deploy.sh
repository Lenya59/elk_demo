#!/bin/bash
function generate_post_data() {
    cat <<EOF
{
    "version": "${1}",
    "description": "${@:2}",
    "timestamp": "$(date +%Y-%m-%dT%H:%M:%S%:z)",
    "maintainer": "mr. rainbow"
}
EOF
}

if [ -z "${1}" ]; then
  echo ERROR. specify app version
  echo -e '\t1.0 - stable app'
  echo -e '\t2.0 - app with AI'
  echo -e '\t3.0 - 500 error bug'
  echo -e '\tanything else - stable app'
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