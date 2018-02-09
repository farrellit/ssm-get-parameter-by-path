import boto3, os

more = None
args = dict(Path=os.environ.get('SSM_PATH'), WithDecryption=True)
ssm = boto3.client('ssm')
parameters = []
while more != False:
    if more:
        args["NextToken"] = more        
    res = ssm.get_parameters_by_path(**args)
    parameters.extend(res['Parameters'])
    
    more = res.get("NextToken", False)
for secret in parameters:
    print("%s: %s", secret["Name"], secret["Value"])
