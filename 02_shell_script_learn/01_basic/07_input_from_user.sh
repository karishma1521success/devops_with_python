#!/bin/bash

# INPUT FROM USER
#SYNTAX -- 
#  read variableName

# Not right way to take an input as user don't know what type of input he is asking . He might can enter integer instead of string.
#after taking an input you want your cursor in next line-use echo 
#1.Read Basic Value from User
read name   
read age

echo "My name is ${name} and my age is ${age}"

read             
# if you don't give variable name as per the syntax it stores the input in REPLAY variable(system defined variable)
echo ${REPLAY}

#IMP *****************************************************
#2. Read With Prompt Message
# If you want to give a message while taking an input you can use prompt
#syntax --  
# read -p "input message to take an input" variableName
read -p "Enter your Full Name " fname  
echo "My full Name is ${fname}"
#best way to take an input

#IMP ***********************************************************
#3. Read Secret Text With Prompt Message
#When you want to take password as input then you have to secure it
#-s flag will hide the characters entered by user
#syntax -- read -p "message" -s secureVariableName
read -p "Enter your password " -s password
echo
read -s -p "Enter your adminId " adminId
#after taking an input you want your cursor in next line-use echo 
echo 
echo ${password}
echo ${adminId}