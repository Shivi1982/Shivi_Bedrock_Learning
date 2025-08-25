# Fully Managed Service: 
1. Fully Managed service:  fully managed service that makes foundation models (FMs) from Amazon and leading
AI startups available through an API
## Key Features: 
1. *Choice and flexibility of FMs:* FM from Amazon and leading AI startups as well as other open source models from Bedrock Market place

2. Provisioned throughput for FMs: provision an instance of anFM that is dedicated to them, have availability and performance SLAs so there is less suprise

3. Access FMs through a single API: single API to securely access customized FMs andthose provided by Amazon and other AI companies.

4. Amazon Bedrock playground: before doing a heavy investment, Amazon gives a playground to test the FMs

5. Model customization: Amazon Bedrock makes a separate copy of the base FM that is accessible
only to you and trains this private copy of the FM using your data that is stored in an Amazon
Simple Storage Service (S3) bucket. None of your data is used to train the original base FMs.We can do this using: 
    - Fine Tuning
    - Prompt Engineering
    - Distillation

6. Agents: Autonomous gives you the ability to build and configureautonomous agents, this includes advanced features like memory management, access management, Bedrock Guardrails and monitoring.

7. Fully Managed RAG support: Bedrock Knowledge Bases is a fully managed capability thathelps you implement the entire RAG workflow from ingestion to retrieval and prompt augmentation 

8. AI Policy Guardrails: Guardrails evaluates user inputs and FM
responses based on use case specific policies, and provides an additional layer of safeguards regardless of the underlying FM. Support toxicity detection, prevent factual errors from hallucinations 

9. Security:
    - data – including prompts, information used to supplement a prompt, FM responses, and customized FMs – remain in the Region where the API call is processed
    - data is encrypted in transit with a minimum of TLS 1.2 (Transport Layer Security) and at rest with either a service-managed AWS Key Management Service (AWS KMS) keys or a customer-managed KMS key

10. Fully-managed experience: don’t need to manage the infrastructure. 

11. Governance and auditability: comprehensive monitoring and logging capabilities and tools that can be used to address your governance and audit requirements. Leverage CloudWatch, CloudTrail, and AWS Config. **Some key features include: (CloudWatch)-**
    - Performance Metrics Tracking: 
        - Invocation metrics: Track request counts, latency, and error rates
        - Token usage: Monitor input/output token consumption for cost management
        - Throughput: Measure requests per second to identify bottlenecks
    - Operational Insights:
        - Service quotas: Monitor approach to API rate limits or model quotas
        - Regional availability: Track service health across AWS regions: 
    - Cost Management:
        - Usage dashboards: Visualize Bedrock spending patterns
        - Budget alerts: Set up notifications when costs exceed thresholds
    - Automated Responses:
        - EventBridge integration: Trigger automated responses to specific conditions
        - Auto-scaling triggers: Adjust provisioned throughput based on demand
    **CloudTrail:**
     Audit & Governance
        - Primary purpose: Activity logging, compliance, and security auditing
        - Focus: "Who did what, when, and where?"
        - Data type: API call history and account activity
        - Time horizon: Historical record of actions taken
        - Use cases for Bedrock:
            Tracking which users/roles accessed specific models
            Auditing prompt submissions for compliance
            Investigating security incidents
            Maintaining records of configuration changes
12: Prompt Routing:routes prompt to different foundational models within a model family, helping you optimize for quality of responses and cost.
13. Prompt Caching: Cache frequently used context in prompts across multiple model invocations, remains available for upto 5 minutes . Imp to note: promot caching currently is only available for Only a subset of models from Anthropic and Amazon


## Amazon Nova Models : 
• Amazon Nova Micro, a text only model that delivers the lowest latency responses at very low cost.
• Amazon Nova Lite, a very low-cost multimodal model that is lightning fast for processing image,
video, and text inputs
• Amazon Nova Pro, a highly capable multimodal model with the best combination of accuracy,
speed, and cost for a wide range of tasks.
• Amazon Nova Canvas, a state-of-the-art image generation model.
• Amazon Nova Reel, a state-of-the-art video generation model to crate high quality video from text
and images.
• Amazon Nova Premier, designed for complex tasks and to act as a teacher for model distillation

14. __VERY IMP : NO ACCESS TO CUSTOMER DATA FOR TRAINING OF BASE MODELS__       
***MODEL DEPLOYMENT ACCOUNTS:***
    - Amazon Bedrock has a concept of a Model Deployment Account – there is one such deployment account
per model provider per AWS Region where Amazon Bedrock is available. These accounts are owned and
operated by the Amazon Bedrock service team, and model providers do not have any access to those
accounts – there is also no outbound or inbound access to or from the Internet for these accounts.
<font color = "red"> Amazon Bedrock will perform copy of a model provider’s inference and training container images intothose accounts, storing them within an Amazon S3 bucket.</font> This copy process will enforce a certain quality bar prior to copying, and it will contain several end-to-end tests and checks to ensure security and compliance within the container image. Amazon Bedrock will have access to these accounts only via narrowly scoped APIs - these assume pre-defined AWS Identity & Access Management (IAM) roles that will
provide appropriately scoped permissions to access various resources in the Model Deployment Account.


15. __Another IMportant Concept__: 
    - **at a high level how does data come to bedrock through few options**
    1. Basically we start with <font color = "Dark yellow">__Customer Environment Components:__ </font>
        - Customer AWS Account: Your AWS account containing all your resources
            - Contains your VPC, security configurations, and IAM roles/permissions
        - Customer VPC (Virtual Private Cloud): Your isolated network segment within AWS
            - Has private IP address range
            - Contains your application servers, databases, etc.
        - Security Groups: Stateful firewall rules at the instance level
        - Network ACLs: Stateless firewall rules at the subnet level
        - Customer IAM Roles: AWS Identity & Access Management (IAM) roles and policies
            - Define permissions for accessing AWS services
        - Customer Data: Your sensitive information stored in S3 buckets, databases, etc.- 
    2. Then we have Connection Methods:           
        2.1 <font color= "#7024FF">Path 1: Public Internet Route: </font>
            - Application sends request within VPC
            - NAT Gateway translates private IPs to public IPs (enabling outbound internet access)
            - Internet Gateway serves as the VPC's connection to the
            -Traffic flows:<font color="Dark Pink">  Application → NAT Gateway → Internet Gateway → Public Internet → Bedrock API </font>
        Why Someone wold use this route: 
            - Simplicity: Easiest to set up with minimal configuration
            - Flexibility: Works from any AWS resource that can access the internet
            - Cost-effectiveness: For lower-volume applications where dedicated connections aren't justified
            - Testing/Development: Quick to implement for proof-of-concept work

        2.2 <font color= "#7024FF">Path 2: VPC Endpoint Route (PrivateLink): </font>
            - Traffic flows: Application → VPC Endpoint → AWS Private Network → Bedrock API
        Why someone would use this:
            - Enhanced Security: Traffic never leaves AWS network
            - Data Privacy: Sensitive data never traverses public internet
            - Compliance Requirements: Meets stricter regulatory requirements
            - Consistent Performance: Avoids internet congestion
            - No NAT Gateway costs: Reduces infrastructure costs.    
        2.3 <font color= "#7024FF">Path 3: Direct Connect Route: </font>
            - Traffic flows: Corporate Device → Corporate Network → Direct Connect Gateway → AWS Private Network → Bedrock API
        Why someone would use this:
            - Low Latency: Direct, dedicated connection for real-time applications
            - High Bandwidth: Suits high-volume, large-data applications
            - Consistent Performance: Avoids internet congestion
            - Regulatory Compliance: For highly regulated industries

# Security & Compliance:
16. _best practices for security and compliance:_
    1. Shared Responsibility Model: 
        - AWS is responsible for protecting the infrastructure that runs all of the services offered by Amazon Bedrock including : Hardware / Global Infrastructure, configuring encryption at rest, responsible for identity and access management configuration
        - Customer is responsible for managing and encrypting their data, as well as applying the correct user access controls to their data and API calls made to Amazon Bedrock.
    2. Network Interactions and VPC Endpoints : 
    example of how it works: 
        - You create specific private tunnels (endpoints) only to certain Bedrock features
        - For example, you might create an endpoint to text generation but not to image generation
        - Your applications can use these private tunnels to reach only those specific features
        - Even if a user has IAM permissions for other features, they physically cannot reach them because the tunnel doesn't exist
        - No internet access or NAT Gateway is needed
    3. Inter-network traffic privacy: All communication with the Amazon Bedrock endpoints is done via HTTPS
endpoints, and all endpoints in all supported regions only support HTTPS - they do not support HTTP communication. Hence, all communication is digitally signed for authentication and integrity
    4. Along with multiple ways to set up IAM policies, it also allows to set something called as __federated users.__:
        - federated users are you can use existing user identities from AWS Directory Service, from your enterprise user directory, or from a web identity provider.  


