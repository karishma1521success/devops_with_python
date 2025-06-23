if [ condition ]
then
#set of statements if the condition is true
else
#set of statements if the condition is false
fi



x=10
y=10
if [ $x -ne $y ] 
then
echo "Not equal"
else
echo "They are equal"
fi