#!/bin/bash

docker run --rm -v $(pwd):/data -ti node /bin/sh -c 'cd /data; npm install'
