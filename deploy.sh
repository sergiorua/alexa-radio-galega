#!/bin/bash

[ -x ./node_modules/serverless/bin/serverless ] || ./install.sh
docker run --rm -e SLS_DEBUG='*' -v $HOME/.aws:/root/.aws -v $(pwd):/data -ti node /bin/sh -c 'cd /data; npm run deploy'
