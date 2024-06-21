#!/bin/bash

#Command Line arguments in shell script - Arguments are inputs that are necessary to process the flow. Instead of getting input from a shell program or assigning it to the program, the arguments are passed in the execution part.
#args which is given with execution command
# ./fileName args1 args2 args3
#    0        1      2     3
echo ${0}   #./fileName
echo ${1}   # args1
echo ${2}   # args2

# Positional Parameters
# Command-line arguments are passed in the positional way i.e. in the same way how they are given in the program execution.
# starts from 0 and go to the nth position
file=${0}    # assigning command line arguments in variables
name=${1}
age=${2}
echo "${file} , ${name} , ${age} "

# ./filename karishma gupta 21
#   0          1       2   3
echo "My name is ${1} and my age is ${2}"
#Then age will print as gupta because it takes gupta as 2nd index argument

#if your argument has space between like karishma gupta then keep it within quotes
# ./filename "karishma gupta" 21
