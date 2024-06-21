#!/bin/bash

#comments"
#PRINTING MESSAGE WITH ECHO COMMAND
echo "This is our first shell script"  #Inline comments"

echo "heyy how are         you"  #This will print same as it is   heyy how are        you. 
echo 'hey how are         you'   # This will print same as it is  heyy how are      you 


echo heyyyy how are         you   #It will print heyyy how are you"
# means it will ignore all the spaces just keep one space.


#PRINTING MESSAGE EACH WORD IN NEW LINE WITH ECHO COMMAND
echo "Hi
I
am 
karishma"
# This will print same as it is each word in new line

#PRINTING MESSAGE IN SINLE LINE IRRESPECTIVE THEY ARE WRITTEN IN NEW LINES
echo "hi \   
I \  
am \
karishma \ 
"
# \ (backslash) represents that don't go to the next line
# it will add hi , I , am , Karishma in single line
#hi I am karishma

# '' - STRONG QUOTES
echo 'hi \   
I \  
am \
karishma \ 
'
#echo with '' print message as it is
# hi \
# I \
# am \
# karishma \


# PRINTING COLOURED MESSAGE
echo -e "\033[0;31m Fail message here"     #\033[0;31m  - make message red
echo -e "\033[0;32m Success message here"  #\033[0;32m  - make message green
echo -e "\033[0;33m Warning message here"  #\033[0;33m  - make message yellow