# Single Stream Audio Skill (My Radio)

This skill demonstrates how to create a single stream audio skill.  Single stream skills are typically used by radio stations to provide a convenient and quick access to their live stream.

User interface is limited to Play and Stop use cases.

## Usage

```text
Alexa, play my radio

Alexa, stop
```

## Installation

You will need to comply to the prerequisites below and to change a few configuration files before creating the skill and upload the lambda code.

### Pre-requisites

This is a NodeJS Lambda function and skill definition to be used by [ASK CLI](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html).

0. You need an [AWS account](https://aws.amazon.com) and an [Amazon developer account](https://developer.amazon.com) to create an Alexa Skill.

1. You need to install and configure the [AWS CLI](https://aws.amazon.com/cli/)

```bash
$ pip install awscli
$ aws configure # https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
```

2. You need to install and to initialize [ASK CLI](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html) with 

```bash
$ ask init
```

3. You need to download NodeJS dependencies :

```bash
$ (cd lambda && npm install)
```

4. This example using Alexa SDK for NodeJS v2 is using [Typescript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html), you need to install Typescript compiler

```bash
$ npm install -g typescript
$ (cd lambda && tsc)
```

### Code changes before deploying

1. ```./skill.json```

   Change the skill name, example phrase, icons, testing instructions etc ...

   Remember than most information is locale-specific and must be changed for each locale (en-GB and en-US)

   Please refer to https://developer.amazon.com/docs/smapi/skill-manifest.html for details about manifest values.

2. ```./lambda/src/AudioAssets.ts```

   Modify each value in the ```AudioAssets.ts``` file to provide your skill with the correct runtime values for values : your radio name, description, icon and, obviously, URL of your stream (https only).

   ```startJingle``` is an optional property defining a Jingle to be played before the live stream. 

   Be sure to modify the value for each language supported by your skill.

   To learn more about Alexa App cards, see https://developer.amazon.com/docs/custom-skills/include-a-card-in-your-skills-response.html

```typescript
let en = {
    card: {
        title: 'My Radio',
        text: 'Less bla bla bla, more la la la',
        image: {
            largeImageUrl: 'https://alexademo.ninja/skills/logo-512.png',
            smallImageUrl: 'https://alexademo.ninja/skills/logo-108.png'
        }
    },
    url: 'https://audio1.maxi80.com',
    startJingle: 'https://s3-eu-west-1.amazonaws.com/alexa.maxi80.com/assets/jingle.m4a'
};
```

3. ```./models/*.json```

   Change the model definition to replace the invocation name (it defaults to "my radio") and the sample phrases for each intent.  

   Repeat the operation for each locale you are planning to support.

4. ```./lambda/src/Constants.ts```


```typescript
export const Constants = {

    // when true, the skill logs additional detail, including the full request received from Alexa
    debug : true,

    // when defined, it tries to read / write DynamoDB to save the last time Jingle was played for that user
    // this allows to avoid to repeat the jingle at each invocation 
    jingle : {
        // the name of the dynamoDB table
        databaseTable : "my_radio",

        // the elasped time between two jingles for a customer (in seconds) 
        playOnceEvery : 1 * 60 * 60 * 24 // 24 hours
    }

});
```

When playing a jingle before your stream, you can choose the name of the database table where the "last played" information will be stored.  If the table does not exist, the persistence code will create the table at the first invocation of the skill.

You can manually create the DynamoDB table with the following command:

```bash
aws dynamodb create-table --table-name my_radio --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

To minimize latency, we recommend to create the DynamoDB table in the same region as the Lambda function.

When using DynamoDB, you also must ensure your Lambda function [execution role](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) will have permissions to read and write to the DynamoDB table.  Be sure [to add the following policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) to the Lambda function [execution role](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "sid123",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:YOUR_ACCOUNT_ID:table/my_radio"
        }
    ]
}
```

### Local Tests

This code uses [Mocha](https://mochajs.org/) and [Chai](http://chaijs.com/) to test the responses returned by your skill.  Be sure you have no test failures before deploying.

Execute your test by typing 

```bash
$ (cd lambda && npm test)
```

Note : if you are deploying in another AWS region than us-east-1, be sure to have an environment variable defined :

```bash
AWS_REGION=<your aws region>
```

### Deployment

ASK will create the skill and the lambda function for you.

Lambda function will be created in ```us-east-1``` (Northern Virginia) by default.

You deploy the skill and the lambda function in one step :

```bash
$ # when you modified the code, be sure to recompile the Typescript code to Javascript
$ (cd lambda && tsc)

$ # Otherwise, just deploy
$ ask deploy
```

IMPORTANT : ask CLI will create an ```index.handler``` lambda entry point by default.  This projects uses typescript and the executable sources are now in the ```lambda/dist``` directory, so it is important to update the Lambda function configuration with the correct code entry point.  You can do this using the AWS command line :

```bash
aws lambda update-function-configuration --function-name ask-custom-My_Radio-default --handler dist/index.handler --runtime nodejs8.10
```

You can test your deployment with

```bash
 $ ask simulate -l en-GB -t "play my radio"
 
 ✓ Simulation created for simulation id: 4a7a9ed8-94b2-40c0-b3bd-fb63d9887fa7
◡ Waiting for simulation response{
  "status": "SUCCESSFUL",
  ...
 ```

You should see the code of the skill's response after the SUCCESSFUL line.

## On Device Tests

To invoke the skill from your device, you need to login to the Alexa Developer Console, and enable the "Test" switch on your skill.

See https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html#step-4-test-your-skill for more testing instructions.

Then, just say :

```text
Alexa, open my radio.
```
