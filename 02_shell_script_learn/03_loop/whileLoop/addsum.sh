#!/bin/bash

# Program to add 2 variables until the sum of both values should be under 20 and print the sum

x=4
y=5
sum=$((x + y))


while [ "$sum" -lt 20 ]
do 
echo $sum

x=$((x + 1))
y=$((y + 1))
sum=$((x + y))

done