# discord-slash

### Content
* Python 3.8 AWS Lamba style function
* AWS CDK Script to deploy the python function into an AWS Lambda

### What does this repo allow you to do at this moment
Provide an endpoint to run [Discord Slash Commands](https://discord.com/developers/docs/interactions/slash-commands), provided the discord application already had been given access to a certain server. This repo, nor the readme will (at the time of writing) not go through the process of creating and deploying the commands. This might be incorporated in a future release. It is *highly* recommended you read through that extensive interactions page to figure out what is going on.

### Requirements:
* [Python 3.8](https://www.python.org/downloads/) or higher
* [NodeJS](https://nodejs.org/en/) >= v13. v14 LTS or higher recommended
* AWS Account, check [Deployment](###Deployment) 
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html)
* [Docker](https://www.docker.com/products/docker-desktop) (requires  Docker account)
* [A Discord Application](https://discord.com/developers/applications/)

### Recommended
[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
[AWS Toolkit for Pycharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-toolkit.html)
I can highly recommend PyCharm as it will make development very easy combined with the AWS Toolkit. Whereas you can use console commands to deploy functions using SAM CLI as well, it is a simple few clicks using the toolkit.

### Configuration
You need to have a Discord Application, at the time of writing it is recommended to activate a Bot as well to avoid most permissions troubles. It is recommended to set the bot private so you control access to the server. The roles and channel ids are hardcoded in discord_config.py as this primarily serves the Jaeger Events Discord. The assumption will be made that you area aware how to run the OAuth2 Process yourself. The only configuration available is through the cdk.json to change the public key of the bot.

### Deployment
For deployment [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is used. This requires you to have an AWS account. The application doesn't use anything outside of the aws free tier. Read more at [Notes](###AWS_Notes).

There are two ways you can call CDK commands. Globally or through NPX commands defined in the package.json. It is recommended to use NPX to govern what CLI version is used through the package.json.

In the directory containing the CDK package.json script run the following commands:

* `npm install` to install all npm packages.
* `npx cdk bootstrap` if you are using CDK for the first time.
* `cdk synth`  to check if any errors are at place.
* `cdk deploy` to start the stack

This will build the lambda function in a container, deploy it to S3 and start up an API Gateway with with a lambda integration at `/DiscordIntents`. The easiest way to figure out the rest of the URL is to go to API Gateway details in the AWS Web Console and find the Invoke URL. `https://<API_ID>.execute-api.<REGION>.amazonaws.com`
This URL with `/DiscordIntents` will have to be provided at the General Information page at your discord application at `Interactions Endpoint URL`. Discord will immediately try and perform a post request to validate the URL accepts valid or invalid signatures. They will not allow you to save the endpoint until it validates your own validation!

### AWS Notes
The [AWS Web Console](https://console.aws.amazon.com/) can be found here. Tutorials on AWS will often refer to this as the AWS Console.

AWS accounts require you to use a credit card to sign up, even if you only use the free tier.

It very much recommended to set a [Budget](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html#free-budget)  with an alert that emails you if a threshold is reached, like $10. AWS Cloudformation, CDK and even just the general AWS Console are *very* powerful tools and you can easily spin up things that incur costs you *can't* afford.

Be sure to check what is included in the [Free Tier](https://aws.amazon.com/free/). For this particular project that means that after 12 months, S3 (to deploy CDK/Functions) and API Gateway will start costing money. Whereas this will still only cost around $1.25 per month, it is good to keep it in mind.
