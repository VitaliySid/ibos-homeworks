#!/bin/bash
#Напишите скрипт, который принимает один параметр и определяет, какой объект передан этим параметром (файл, каталог или не существующий). 
#**Например:**
#**user@user:~$ ./test.sh /etc**  
#**/etc - dir**  
#**user@user:~$ ./test.sh /etc/passwd**  
#**/etc/passwd - file**  
#**user@user:~$ ./test.sh /etc/passwd1**  
#**/etc/passwd1 - not exist**  

if [ -d $1 ]
then
echo "$1 - dir"
elif [ -f $1 ]
then
echo "$1 - file"
else
echo "$1 - not exist"
fi