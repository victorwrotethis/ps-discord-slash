import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';
import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Alias, Runtime, Version } from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import { Config } from './config';
import { HttpLambdaIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import { HttpApi, HttpMethod } from 'aws-cdk-lib/aws-apigatewayv2';

export class AwsCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const discordApi = new HttpApi(this, 'DiscordApi');

    const interactionsHandler = new PythonFunction(this, 'InteractionsHandler',{
      functionName: 'DiscordInteractions',
      entry: '../ps-discord-slash-python/main',
      index: 'gecore/ps_discord_slash/app.py',
      handler: 'lambda_handler',
      runtime: Runtime.PYTHON_3_9,
      environment:{
        discord_public_api_key: Config.discordPublicApiKey,
        ovo_web_url: Config.ovoWebUrl,
        token_api_url: Config.tokenApiUrl
      }, currentVersionOptions: {removalPolicy: RemovalPolicy.RETAIN}      
    });
    const versionLa = new Version(this, 'VersionIH4', {lambda: interactionsHandler, description: 'adds nothing again', removalPolicy:RemovalPolicy.RETAIN});
    const aliasLa = new Alias(this, 'AliasIH4', {version: versionLa, aliasName: 'V5'})//should be named live/prod/active/blue/green/debug etc
    const interactions_integration = new HttpLambdaIntegration('DiscordIntegration',interactionsHandler);

    discordApi.addRoutes({
      path: '/DiscordInteractions',
      methods: [HttpMethod.POST],
      integration: interactions_integration
    });

  }
}
