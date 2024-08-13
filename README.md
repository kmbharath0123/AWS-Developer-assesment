# AWS-Developer-assesment-DXC
Hello Bharath

Hope you are doing good!

 

I have shared you the assignment below, kindly read the instructions carefully first and then start your assignment.

Please let me know if you have any questions.

 

Pre-requisites:

Personal AWS Account
Personal GitHub account
 

This task is designed to evaluate your skills in AWS development and project delivery.

1) **Open the AWS System Manager Parameter Store from the AWS Console, and create the following parameter using Standard Tier of type String:
         Name: UserName
         Value: JohnDoe        --------------------------- completed **

 

2)**From the AWS Console, create an S3 bucket to be used in the next step.**   ------------------ completed 
 

3)Using a single AWS CloudFormation template (YAML or JSON), write a custom Lambda function in Python or Java called “exercise-lambda” that will:

**Retrieve SSM Parameter Store the key/value pair created above in step 1 ---------------------- completed
Store this retrieved key/value pair into a file in the S3 bucket created in Step 2.  -------------- completed**
Hints:

-       don’t forget to send a response back from the custom Lambda function to CloudFormation.

-       Be sure to handle Delete events in order to prevent hangs during stack deletion

-       Be sure to grant appropriate permissions (not excessive permissions) to the lambda function so that CloudWatch logs will be created during stack creation.  These logs can be used for troubleshooting the lambda function. 

-       Do not choose an IAM role in CloudFormation – Configure stack options when creating the stack.  The CloudFormation template should define any necessary permissions.

 

Upload the completed CloudFormation Template and Lambda function to GitHub (don’t make is private), and provide us the repo URL for validation.
 

We are interested in determining your overall abilities, so you may provide into your GitHub repo as much code as you have completed, even if the exercise is not complete. 

Relax, and have fun.
