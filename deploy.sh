#!/bin/bash

dockerImage="nikolaik/python-nodejs:python3.7-nodejs10"
stage=${1:-dev}

[ -x ./lambda/py/node_modules/serverless/bin/serverless ] || ./install.sh
docker run --rm -e SLS_DEBUG='*' -v $HOME/.aws:/root/.aws -v $(pwd):/data -ti $dockerImage /bin/sh -c "cd /data/lambda/py; npm run deploy-${stage} && ./node_modules/serverless/bin/serverless s3deploy --stage ${stage}"
