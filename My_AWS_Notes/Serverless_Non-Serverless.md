# 1. Serverless LLM Models: 
**Definition:**
- You do not provision or manage any dedicated compute for the model.
- You just call the API, AWS spins up the resources to serve your request, runs the inference, and tears it down after.

**Key traits:**

- Pay-per-use — You pay for tokens processed (input + output).
- No capacity planning — AWS auto-scales for you.
- No idle cost — You’re not billed if you’re not making requests.
- Cold starts possible — First request after inactivity may be slightly slower.
- Stateless — Each request is independent unless you pass prior messages as context.

**Bedrock example:**
- Most Anthropic Claude, Amazon Nova, and Mistral models in Bedrock today are serverless — you just call bedrock-runtime.invoke_model(...) and AWS handles hosting.


# 2. Non-Serverless (Provisioned Throughput / Dedicated) LLM Models
__Definition:__
    - You reserve dedicated model capacity (compute) for your use only.

__Key traits:__
- Capacity guaranteed — No sharing, predictable latency.
- Always running — No cold starts.
- Fixed cost — You pay for the reserved capacity whether you use it or not.
- Better for high-volume / low-latency workloads — e.g., chatbots with thousands of concurrent users.
- Configuration — You select the model, throughput (tokens/sec), and AWS deploys dedicated endpoints.
- SLA Coverage: Typically comes with stronger service level agreements

__Bedrock example:__
    - Amazon Bedrock’s Provisioned Throughput for Claude Opus or Llama 3.1 — you pay a monthly/hourly fee for reserved capacity.