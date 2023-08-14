import os
from aws_cdk import App
from aws_cdk import Environment
from cdk_infrastructure.lambda_function.stack import IngestionLambdaStack
from cdk_infrastructure.s3_buckets.stack import S3DeployStack
from cdk_infrastructure.s3_buckets.constants import BUCKET_NAMES
from dotenv import load_dotenv

load_dotenv()

env = Environment(
    account=os.environ.get("AWS_ACCOUNT_ID"),
    region=os.environ.get("AWS_REGION_NAME"),
)

app = App()

IngestionLambdaStack(
    app, "LambdaIngestionStack", image_name="budget-guard", env=env
)

for bucket_name in BUCKET_NAMES:
    S3DeployStack(app, f"{bucket_name}Stack", bucket_id=bucket_name, env=env)


app.synth()
