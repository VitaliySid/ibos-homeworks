#!/bin/bash
#Напишите скрипт, который принимает один параметр и определяет, какой объект передан этим параметром (файл, каталог или не существующий). 
#**Например:**
#**user@user:~$ ./test.sh /etc**  
#**/etc - dir**  
#**user@user:~$ ./test.sh /etc/passwd**  
#**/etc/passwd - file**  
#**user@user:~$ ./test.sh /etc/passwd1**  
#**/etc/passwd1 - not exist**  

if ($args.Count -eq 0) {
    "incorrect input"
    exit
}

if (-not (Test-Path $args[0])) {
    "{0} - not exist" -f $args[0]
    exit
}

$target = get-item $args[0]
if ($target.PSIsContainer) 
{ "{0} - dir" -f $args[0] }
else 
{ "{0} - file" -f $args[0] }