#!/bin/bash
 # There should not be any space around the “=” sign in the variable assignment.
 # VariableName=value
#  When you use VariableName = value, the shell assumes that [VariableName is the name of a command and tries to execute it.}

# variables are of two types in shell scripting :   1. user defined variable     2. system defined variables.
#user defined variables
name="karishma"  #don't give space around = in shell scripting
age=21           # $ dollar sign - to use variable in program
# name = "karishma"  -- will not work

#system defined variables
#IMP ****  USING env command you can see all the system defined variables
echo ${HOME}  #Give path 
echo ${OSTYPE} #type of os 
echo $PATH
echo ${$}        # Process ID
echo ${PPID}     # Parent Process ID
echo $PWD        # Path of present working directory
echo $HOSTNAME   # name of host
echo $UID        # User ID  
# UID = 5000    cannot changed - UID is a read only variable.


# IMP ***************************
#two ways to use variables in program
#1.   $variableName        2.    ${variableName} - best way
echo $name     # karishma
echo ${name}   # karishma -- the best way to use variable

echo "My name is ${name} and age is ${age}"
echo 'My name is $name and age is $age'  # this will print same message as it is
# My name is $name and age is $age





#Documentation*******************************************

# Variable - 1. A variable is a container that holds data
#            2. A variable is nothing more than a pointer to the actual data.
#            3. Variables are case sensitive


# RULES************************************************
# The name of a variable can contain only letters (a to z or A to Z), numbers ( 0 to 9) or the underscore character ( _).
# Variable names cannot be reserved words
# Variable names cannot have whitespace in between
# The variable name cannot have special characters.The reason you cannot use other characters such as !, *, or - is that these characters have a special meaning for the shell.
# The first character of the variable name cannot be a number.
# By convention, Unix shell variables will have their names in UPPERCASE.

# The following examples are valid variable names
# _VARIABLE_NAME   VARIABLE_NAME  VARIABLE_1_NAME   vARIABLE_2_NAME

# Following are the examples of invalid variable names
# 2_VARNAME    -VARIABLENAME    VARIABLENAME-SOMENAME   SOMENAME_A!


#IMP ****************************************************
# Defining Variables
# variable_name=variable_value
# For example −   MY_MESSAGE="Hello World"
