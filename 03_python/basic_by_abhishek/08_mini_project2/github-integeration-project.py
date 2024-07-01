import requests
# project - Get pull request information on a github repo(let's say kubernates repo) using python
# output - pull request creators name with their counts
# step 1 . import requests using pip install requests command so that we can make a request call to github

#step2.  Making api call to github
# url to fetch pull requests  from the github API

# url structure to pull request -   https://api.github.com/repos/OWNER/REPO/pulls
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# making GET request to fetch all pull request data from the github API
response = requests.get(url)
print(response)   
#<Response [200] - we should get this response (means successful fetching the data)
# <Response [404]> -  means not found error - something is wrong in url 
# <Response [500]> - means internal server error - something is wrong in the server side

if response.status_code == 200:
    # convert the json response to a directory - response.json()
    pull_requests_list = response.json()  # output - list of directory
    # print(data)  # it will print whole list of directory

    # create an empty dictionary to store pr creators and their count
    pr_creators = {}
    
    for pull in pull_requests_list:
        # pull - 0 index dictionary so on
        creator = pull["user"]["login"]

        # checking key of creator name is present or not
        if creator in pr_creators: 
            # true means that creator already make pull request before
            # increase count
            pr_creators[creator] = pr_creators[creator] + 1
        else:
            # false that creator make pull request first time
            # add creator name and count 1 in dictionary pr_creators
            pr_creators[creator] = 1
    
    # print creator name with request count he made
    # print(pr_creators)
    for key, value in pr_creators.items():
        print("Creator - ", key, "  Requests- " , value)
else:
    print("failed to fetch data. status code: ", response.status_code)



