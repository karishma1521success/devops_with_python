# Boto3 is a package in python 
# used for automation to build services in aws (ec2, s3)


@ You know we have many automation tools
1. cft (cloud formation template)
2. terraform 
3. aws cli
4. boto 3 

**** imp **********************************************
# for better automation - have good knowledge of aws manual steps to create services
*                       ||
    aws cli             ||                  cft 
    boto3               ||                  terraform
*  (scripting )         ||               (template)        

# aws cli and boto 3 are automation tool which is done by scripting (programming commands)

# cft and terraform are automation tools which is done by using templates (create templates to build infrastructure)

Ques. why do we want aws cli or boto 3 if we already have aws cft and terraform for automating the services 

Ans.  
1. aws cli and boto 3 has some commands which give quick response such as  (aws s3 ls) - give list of s3 instantly

advantage of boto3 over aws cli ***********************************************************************
# boto3 is needed because it is used in serverless programming - (lamda functions (which is required in cost optimization, monitoring and notifications))  That's why we need python scripting language for automation

2. whereas, cft and terraform use template which contains many steps like installing terraform, setup terraform files, authetication etc to get information or to create resources in aws -- (delayed response)


