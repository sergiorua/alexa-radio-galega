#!/bin/bash

# Built using ./docker/Dockerfile
dockerImage="python3.11-nodejs10"
stage=${1:-dev}

[ -x ./lambda/py/node_modules/serverless/bin/serverless ] || ./install.sh

(cd lambda/py/locales && ./compile.sh)

docker run --rm -e SLS_DEBUG='*' -v $HOME/.aws:/root/.aws -v $(pwd):/data -ti $dockerImage /bin/sh -c "cd /data/lambda/py; npm run deploy-${stage} && node ./node_modules/serverless/bin/serverless.js s3deploy --stage ${stage}"
