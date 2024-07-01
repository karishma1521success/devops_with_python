

# function to update server config which take file , key and value as parameter
def update_server_config(filePath, updatedKey, updatedValue):
    #1. open file and read all lines 
    with open(filePath,'r') as file:
        fileLines = file.readlines()
        print(fileLines)

    
    # 2. open file in write mode and update MAX_connections
    with open(filePath,'w') as file:
        for line in fileLines:
            # check update key present in line 
            if updatedKey in line:
                # present update key
                file.write(updatedKey + "=" +updatedValue + "\n")
            else:
                # not present keep the line as it is
                # if you do not write else part it will remove all file which doesn't contain updated key
                # max_connections = 500 will left and all lines will get remove if no else part
                file.write(line)


                
       



filePath = "03_python/basic_by_abhishek/09_mini_project/server.conf"
updatedKey = "MAX_CONNECTIONS"
updatedValue = '1000'
update_server_config(filePath ,updatedKey, updatedValue )
