#!/bin/bash
# Напишите два скрипта, каждый из которых принимает один параметр и:
#- первый - прибавляет к параметру единицу как строку.
#  **Например:**  
# **user@user:~$ ./test_1.sh 5**  
#  **51**  

if [ -z $1 ]
then
   echo "Нет аргументов"
else 
   echo "${1}1"
fi