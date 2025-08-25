# WHAT ARE TRUSTED POLICIES:

**For Bedrock to access any other tool like SageMaker or Q or S3, we can assign a trusted policy. this means AWS Bedrock service itself is allowed to call sts:AssumeRole on this role.**

1. WHY DO WE NEED IT : 
    - In AWS, when a service (like Bedrock or SageMaker) needs to act on your behalf — for example:
        - Bedrock calling other AWS services (S3, DynamoDB, etc.) in an Agent flow
        - SageMaker running a job that pulls/pushes data from S3
        - Bedrock running custom model inference via SageMaker endpoints
        the service must assume an IAM role that has the needed permissions.
    **REMEMBER: this is different from the user-level permissions we discussed earlier.**
    

    **this only tells AWS that the bedrock service is allowed to assume this role. it does not give any permissions to the user.** for humans to still get this permission , Humans (or CI roles) need iam:PassRole (and relevant Bedrock/SageMaker actions) to let the service assume that role on their request.

    2. Here is how we create in Bedrock: 
        - In Bedrock, Go to IAM Roles
        - In the left menu, click Roles.
        - Click Create role →
        - Trusted entity type = AWS service
        - Select Bedrock
        - Sometimes Bedrock is not yet exposed in the console’s “Service or use case” dropdown for role creation.
        - In that case, use the Custom trust policy option and paste the following:
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": [
                            "bedrock.amazonaws.com",
                            "sagemaker.amazonaws.com". # added sagemaker to call bedrock, but if only bedrock is needed we can remove sagemaker 
                        ]
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        ```"bedrock.amazonaws.com", 
                        "sagemaker.amazonaws.com" 
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        ```

    3. The third step is where we attach the right permission policies so the role can actually do something useful.
    4. On next page we can narrow down on the application that would need this assume role 
    5. Select imp options like: 
        - AmazonBedrockFullAccess – full access to Bedrock APIs, including InvokeModel and InvokeModelWithResponseStream.
        - AmazonS3ReadOnlyAccess – read-only access to S3 (if Bedrock needs to read data from S3)
        - AmazonS3FullAccess – full access to S3 (if Bedrock needs to read/write data from S3)
        - AmazonDynamoDBReadOnlyAccess – read-only access to DynamoDB (if Bedrock needs to read data from DynamoDB)
        - AmazonSageMakerFullAccess – gives SageMaker the ability to spin up instances, train, and run inference. [f this role will be assumed by a SageMaker Notebook, Studio, or endpoint]
        - If you want logging to CloudWatch:
            - CloudWatchLogsFullAccess


**IN A NUTSHELL, ONCE A USER OR GROUPS ARE CREATED IN BEDROCK AND THEY HAVE RELEVANT PERMISSION, IF THEY NEED TO READ , WRITE OR DO ANYTHING WITH S3 OR ANY OTHER AWS SERVICE, WE NEED TO CREATE A TRUSTED POLICY FOR THAT SERVICE AND ATTACH IT TO THE ROLE THAT THE USER OR GROUP IS ASSIGNED TO.**
