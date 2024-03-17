#!/bin/bash

# Built using ./docker/Dockerfile
dockerImage="python3.11-nodejs10"
# dockerImage=node:8.17.0
docker run --rm -v $(pwd):/data -ti $dockerImage -w /data/lambda/py /bin/sh -c 'npm install'
