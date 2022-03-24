import { Construct, Node } from "constructs";

/**
 * Creates a config class from cdk.json that is approachable through methods.
 */
export class Config {
    static rootNode: Node

    static init(root: Construct) { this.rootNode = root.node; }
    static getConfig<T>(key: string): T { return this.rootNode.tryGetContext(key) as T }

    static get discordPublicApiKey() { return this.getConfig<string>('discordPublicApiKey') };
    static get ovoWebUrl() { return this.getConfig<string>('ovoWebUrl') };
    static get tokenApiUrl() { return this.getConfig<string>('tokenApiUrl') };

}
