# We will get the arn and you have to take out the username from that particular arn

arn = "arn:aws:iam::123456789012:user/johndoe"

username = arn.split("/")[1]
print(username)