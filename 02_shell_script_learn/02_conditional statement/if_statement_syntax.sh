# https://www.geeksforgeeks.org/linux-unix/conditional-statements-shell-script/


if [ condition ]
then
#statements
fi


#!/bin/sh
x=10
y=11
if [ $x -ne $y ] 
then
echo "Not equal"
fi