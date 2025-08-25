#1.  set access keys and id 
# %%
import os
import sys
from pathlib import Path

# Just add the project root to path - works for both cases
current_file = Path(__file__).resolve() if '__file__' in globals() else Path.cwd() / 'initial_invoke.py'
project_root = current_file.parent.parent

print(f"Project root: {project_root}")
sys.path.insert(0, str(project_root))

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from project.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

print("✅ AWS key:", AWS_ACCESS_KEY_ID)
print("✅ AWS secret:", AWS_SECRET_ACCESS_KEY)
print("✅ AWS region:", AWS_REGION)

# =============================================


# %%
import boto3
AWS_REGION = os.environ.get('AWS_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
bedrock= boto3.client(service_name='bedrock-runtime', region_name=AWS_REGION, 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


# =========================================================
# 2. Run a Basic code to see if the connection is working 
# %%
import logging
logging.basicConfig(level=logging.INFO)
# logging has a default configuration- WARNING level as the default threshold.
#but logging.info() and logging.debug() will not appear unless you change the level.
bedrock_mngt= boto3.client(
    service_name='bedrock', 
    region_name=AWS_REGION, 
    aws_access_key_id=AWS_ACCESS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
try: 
    response = bedrock_mngt.list_foundation_models()
    logging.info("List of available Models")
    print ("---" * 10)
    for model in response['modelSummaries']:
        print(f"Model ID: {model['modelId']}")
        print(f"Model Name: {model['modelName']}")
        print(f"Provider: {model.get('providerName', 'N/A')}")
        print (f"Input Modality:{model['inputModalities']}")
        print(f"output Modality: {model['outputModalities']}")
        print(f"Context Window (tokens): {model.get('context_Length', 'N/A')}")
        print ("---" * 10)
except Exception as e:
    logging.error(f"Error listing models: {e}")

#see file codeunderstanding.md for how modelSummaries work 
# =========================================================
# 3. Now Test a basic prompt 

#%%
import json 
my_text = {
    "messages": [
        {
        "role": "user",
        "content": [
            {"text": "IN Clean Bullet- How does bedrock work crewai, langgraph & other agentic providers"}
        ]
    }
],
"inferenceConfig": {
        "maxTokens": 4000,
        "temperature": 0.3,
        "topP": 0.9
    }
}
response= bedrock.invoke_model(
    body = json.dumps(my_text),
    modelId= 'us.amazon.nova-premier-v1:0',
    accept= 'application/json',
    contentType= 'application/json'
)
print(response['body'].read().decode('utf-8'))
# IMP TO NOTE HERE: I HAD TO USE US. prefix for the model id to work. 
#AWS manages compute resources through inference profiles for high-demand models.
#THIS NOVA PREMIER IS ONE OF THE HIGH DEMAND MODEL , REQUIRES SIGNIFICANT GPU, due to
#this Regional optimization: us. prefix routes to optimal US data centers

# ==========================================================
# %% 
#better way to call bedrock model api 
import json 
def nova_models(bedrock,model_id,my_text, max_tokens=4000,temperature=0.3, top_p=0.9):
    user_text = {
        "messages":[
            {"role":"user", "content":[{"text":my_text}]}
        ],
        "inferenceConfig":{
            "maxTokens":max_tokens,
            "temperature":temperature,
            "topP":top_p
        }
    }
    response= bedrock.invoke_model(
        modelId= model_id,
        body = json.dumps(user_text),
        accept= 'application/json',
        contentType= 'application/json'
    )
    data = json.loads(response["body"].read())
    return data["output"]["message"]["content"][0]["text"]
#usage
text = nova_models(bedrock, "us.amazon.nova-premier-v1:0", "What are agent design patterns suggested by AWS Bedrock?Answers in clean bullet points")
print(text)


# =========================================
# %%
#using invoke model with response stream to get live answrs as sson as tokens are generated 
bedrock= boto3.client(
    service_name="bedrock-runtime", 
    region_name=AWS_REGION, 
    aws_access_key_id=AWS_ACCESS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
import json

def nova_models(bedrock, model_id, my_text, max_tokens=4000, temperature=0.3, top_p=0.9):
    user_text = {
        "messages": [
            {"role": "user", "content": [{"text": my_text}]}
        ],
        "inferenceConfig": {
            "maxTokens": max_tokens,
            "temperature": temperature,
            "topP": top_p
        }
    }

    resp = bedrock.invoke_model_with_response_stream(
        modelId=model_id,
        body=json.dumps(user_text),
        accept="application/json",
        contentType="application/json"
    )

    final_text = ""

    for event in resp["body"]:
        if "chunk" in event:
            chunk_data = json.loads(event["chunk"]["bytes"])

            # Nova puts streaming text here:
            if "contentBlockDelta" in chunk_data:
                delta_text = chunk_data["contentBlockDelta"]["delta"].get("text", "")
                if delta_text:
                    print(delta_text, end="", flush=True)  # live stream output
                    final_text += delta_text

    print("\n---\nFinal collected text:", final_text)
nova_models(
    bedrock,
    "us.amazon.nova-premier-v1:0",
    "Summarize the latest AWS Bedrock agent design patterns in bullet points."
)

# %%
