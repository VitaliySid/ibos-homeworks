#!/bin/bash
#Напишите скрипт, который выводит содержимое каталога и подсчитывает в нём количество файлов.
#**Например:**  
#**user@user:~$ ./test_dir.sh  
#admin_scripts**  
#**...**  
#**Videos**
#**Total: 22**     

$names = Get-ChildItem -Path $args[0] -Force

foreach($n in $names)
{ $n.Name }

"Total: " + $names.Count