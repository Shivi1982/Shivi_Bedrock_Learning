# Open source models: 
### this below is Bedrock Marketplace-- 
1. Choose model from Hugging Face catalog
2. SageMaker downloads model files and runs them on GPU servers
3. SageMaker creates an endpoint (API URL) 
4. Bedrock Marketplace registers that endpoint
5. You call the endpoint to use the model

## Basic flow & architecture: 
Code → Bedrock Runtime API → Bedrock Marketplace → SageMaker Endpoint → GPU → Model Response

## why use Bedrock: 
Benefits of Bedrock Marketplace:

- **Unified API**: Same code works for Claude, Titan, AND marketplace models
- **Tool integration**: Works with Bedrock Agents, Guardrails, Knowledge Bases
- **Easier discovery**: Browse models in Bedrock console
- **Consistent format**: All models use same request/response format

### FLOW: 
- To deploy a model

    - Sign in to the AWS Management Console using an IAM role with Amazon Bedrock permissions.
    - In the search bar, specify "Amazon Bedrock" and choose the Amazon Bedrock from the dropdown list.

    - From the navigation pane, choose Model Catalog.
    - Choose the model card for the model that you're deploying.
    - Choose Deploy.
    - For Endpoint Name, specify the name of the endpoint.
    - Choose the number of instances and select the instance type.
    - Under Advanced Settings, you can optionally:
        - Set up your VPC
        - Configure the service access role
        - Customize your encryption settings

