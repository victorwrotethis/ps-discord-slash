import { HttpApi, HttpMethod } from '@aws-cdk/aws-apigatewayv2';
import { LambdaProxyIntegration } from '@aws-cdk/aws-apigatewayv2-integrations';
import { Alias, Runtime, Version } from '@aws-cdk/aws-lambda';
import { PythonFunction } from '@aws-cdk/aws-lambda-python';
import * as cdk from '@aws-cdk/core';
import { RemovalPolicy } from '@aws-cdk/core';
import { version } from 'process';
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
      }, currentVersionOptions: {removalPolicy: RemovalPolicy.RETAIN}      
    });
    const versionLa = new Version(this, 'VersionIH4', {lambda: interactionsHandler, description: 'adds nothing again', removalPolicy:RemovalPolicy.RETAIN});
    const aliasLa = new Alias(this, 'AliasIH4', {version: versionLa, aliasName: 'V5'})//should be named live/prod/active/blue/green/debug etc
    const interactions_integration = new LambdaProxyIntegration({handler: interactionsHandler});

    discordApi.addRoutes({
      path: '/DiscordInteractions',
      methods: [HttpMethod.POST],
      integration: interactions_integration
    });

  }
}
