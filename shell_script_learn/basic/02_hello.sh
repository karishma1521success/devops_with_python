#1. open terminal 
#2. {cd directoryName} Go to desired directory using  command
#3. {vim fileName.sh}  create shell script file 
    #. A new terminal will open 
    #. click i - Go in INSERT mode
    #. Imp - #!/bin/bash  -- shebang 
    #. Write commands like echo , pwd, ls...
    #. click {esc + :wq!+ Enter}  - this will save and terminate the file
#4. {ls -l} - check the file permission so that we can execute our file
    # {chmod +x fileName..sh) -- To change perimission
    # {chmod 777 fileName.sh} -- 777 (given all read write and execute perimisiion to owner, group and everyone)
#5. {./fileName.sh} - To execute a file


#vim hello.sh

#!/bin/bash   
echo "hello"
echo "welcome to shell script world"

ls
pwd
sleep 10 # make program pause for 10 second
echo "message after 10 second pause"
