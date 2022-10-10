#!/bin/bash
#Напишите скрипт, который выводит содержимое каталога и подсчитывает в нём количество файлов.
#**Например:**  
#**user@user:~$ ./test_dir.sh  
#admin_scripts**  
#**...**  
#**Videos**
#**Total: 22**     
cnt=0

for fl in $(ls $1)
do
   cnt=$(( $cnt+1 ))
   echo $fl
done

echo "Total: $cnt" 
