1. **Amazon Bedrock Agents** offers a fully managed solution that automatically orchestrates interactions between foundation models, data sources, software applications, and user conversations. Agents automatically call APIs to take actions and invoke knowledge bases to supplement information

2. **Built-in orchestration**: Default ReAct (Reason and Action) strategy using foundation model's tool use patterns
   - **Automatic planning**: Agent breaks down tasks automatically
   - **Memory retention**: Agents retain memory across interactions for personalized experiences
   - **Knowledge base integration**: Built-in RAG capabilities

**Custom Orchestration Bedrock Agents:**

- **Lambda-based control**: Define custom orchestration logic using AWS Lambda for flexible agent behavior
- **Advanced strategies**: Implement Plan and Solve, Tree of Thought, and Standard Operating Procedures (SOP)
- **State management**: Contract-based interactions between Amazon Bedrock Agents and AWS Lambda with defined states and events

*References:*
- https://aws-samples.github.io/amazon-bedrock-samples/
- https://dev.to/onepoint/how-to-create-a-web-search-ai-agent-with-aws-bedrock-5f1k

**What you still have to build yourself:**

- **Lambda functions**: For external API calls and custom business logic
- **Web search API integration**: Services like Serper, Tavily, or Google Search API
- **Custom orchestration logic**: Lambda-based workflow control and decision making
- **Action group definitions**: Structured API schemas and function mappings


