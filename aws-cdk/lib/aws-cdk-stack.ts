import { HttpApi, HttpMethod } from '@aws-cdk/aws-apigatewayv2';
import { LambdaProxyIntegration } from '@aws-cdk/aws-apigatewayv2-integrations';
import { Runtime } from '@aws-cdk/aws-lambda';
import { PythonFunction } from '@aws-cdk/aws-lambda-python';
import * as cdk from '@aws-cdk/core';
import { Config } from './config';

export class AwsCdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const discordApi = new HttpApi(this, 'DiscordApi');

    const interactionsHandler = new PythonFunction(this, 'InteractionsHandler',{
      functionName: 'DiscordInteractions',
      entry: '../ps-discord-slash-python/main',
      index: 'gecore/ps_discord_slash/app.py',
      handler: 'lambda_handler',
      runtime: Runtime.PYTHON_3_8,
      environment:{
        discord_public_api_key: Config.discordPublicApiKey
      }
    });

    const interactions_integration = new LambdaProxyIntegration({handler: interactionsHandler});

    discordApi.addRoutes({
      path: '/DiscordInteractions',
      methods: [HttpMethod.POST],
      integration: interactions_integration
    });    

  }
}
