bedrock-runtime : Make inference calls to the models (chat, completions , embeddings)
Invoke model: bedrock.invoke_model- sends a single inference request. This is Stateless (no conversation memory on the server).
bedrock - manage models and configurations (list models, get model info, custom models)
bedrock-agent-runtime - Execute and interact with Bedrock agents at runtime
bedrock-agent - Create and manage Bedrock agents and knowledge bases
bedrock-data-automation-runtime - Execute data automation workflows
bedrock-data-automation - Create and manage data automation pipelines
invoke_model_with_response_stream: 
    - Sends the request and starts streaming tokens back as soon as they are generated.
    - You can process or display the text incrementally (like watching ChatGPT “type” in real time
    - Especially useful for:
        - Live chat UIs
        - Long answers where you don’t want the user to wait for the whole response
        - Streaming to logs or real-time processors
Converse- building conversational AI applications. It allows developers to create more natural and engaging interactions between users and AI systems.
- Very imp to know: 
    - There are models which are in high demand and require significant GPU resources. 
    - AWS manages compute resources through inference profiles for high-demand models.
    - **Regional optimization: us. prefix routes to optimal US data centers**
    - one example of such a model is us.amazon.nova-premier-v1:0, 

        