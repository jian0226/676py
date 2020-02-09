#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:54:28 2020

@author: shuaijiang
"""

# URL:https://github.com/jian0226/676py.git

import math

# question 1(a)

# create a list first.
# uss a while loop to count and record number "i" from 1 , each 
# time add "i" into the list until "i" reach 20.
# then, the loop breaks.
# print the list.

mylst = []
i = 0
while i >= 0:
    i = i+1
    mylst.append(i)
    if i >= 20:
        break

print(mylst)
    

# question 1(b)

# create a list.
# use range function and make numbers printed from 20 to 1, each time the 
# number in this sequence is added "-1" from the last number.
# print the list.

mylst2 = list(range(20,0,-1))
print(mylst2)


# question 1(c)

# create a list and combine the 2 lists above into one.
# detect the index of number 20 and delete it.
# print the list.

mylst3 = mylst+mylst2
del(mylst3[(mylst3.index(20))])
print(mylst3)


# question 1(d)

# write a list containing numbers 4,6,3, then let this list * 10.
# the same number sequence will repeat 10 times.
# print the list.

mylst4 = [4,6,3]*10
print(mylst4)


# question 1(e)

# create a list first.
# make a while loop that counts from 0.
# as long as count smaller than 11, "4,6,3"can be recorded into the list.
# when the counter reaches 11, still record "4", but stop recording 6 and 3.
# and loop breaks.
# print the list.

mylst5 = []

count = 0
while count <= 11:
    mylst5.append(4)
    count += 1
    if count <11:
        mylst5.append(6)
        mylst5.append(3)
    else:
        break
    
print(mylst5)
    
    
# question 2

# define a function called fn2 contains variable "num", each time 
# we call function fn2 and type a number, fn2 function will return the 
# result as defined in this function.

# create a list, and write a for loop.
# let "i" count from 3 to 6, each time "i" increases 0.1 from the the last "i",
# by using range function and then dividing the number by 10 in order to 
# get float number. (range function does not apply to float).

# call the function within for loop and append the results into list.

# print list.

def fn2(num):
    return math.exp(num)*math.cos(num)

lst2 = []
for i in range(30,61,1):
    i = i/10
    j = fn2(i)
    lst2.append(j)
    
print(lst2)


# question 3

# define a function named fn3 that contains variable "n", each time 
# we call function fn3 and type a number, fn3 function will return the 
# result as defined in this function.

# create a list.

# write a for loop and use range function to count i from 1 to 25.
# everytime we count an "i", print the result of function fn3 with input "i".
# append the results into the list

#print the list. 

def fn3(n):
    return 2**n/n

lst3 = []
for i in range(1,26):
    j = fn3(i)
    lst3.append(j)
    
print(lst3)


# question 4(a)

# create a list.
# write a for loop that counts i from 0 to 19.
# let j = the ith index of the list - the (19-i)th index of the list
# record j 20 times and print the list.

lst4 = []
for i in range(20):
    j = mylst[i]-mylst[19-i]
    lst4.append(j)
print(lst4)
    

# question 4(b)

# create a list.

# write a for loop and count 1 from 0 to 19 by using range function.
# within the for loop of i, use module calculation:
#   if the ith index within the list is an even number, print True.
#   otherwise, if the ith index within the list is an odd number, print Flase.

# append the result into list.
# print list.

lst4b = []
for i in range(20):
    if mylst[i]%2 == 0:
        j = True
        lst4b.append(j)
    else:
        j = False
        lst4b.append(j)
        
print(lst4b)


# question 5(a)

# open text file.
# read the file.
# make each word into a string within "stri".

# make 3 counters "a","b", and "c", counters count from 0.

# write a for loop, looping by all word within "stri":
#   if the length of a word is larger or euqal to 8, then counter a adds 1.
#   if the length of a word is smaller than 8 but larger or euqal to 4,
#   ,then counter b adds 1.
#   if the length of a word is smaller than 4 but larger or equal to 1,
#   then counter c adds 1.

# print the results with respects to a, b and c.

f = open("lorem.txt","r")
data = f.read()
stri = data.split()

a=0
b=0
c=0

for x in stri:
    if len(x)>=8:
        a = a+1
    elif len(x)>=4:
        b = b+1
    elif len(x)>=1:
        c = c+1
print( "The amount of words which length are greater or equal to 8 is:", a)
print( "The amount of words which length are greater or equal to 4 but smaller than 8 is:", b)
print( "The amount of words which length are greater or equal to 1 but smaller than 4 is:", c)

   
# question 5(b)

# from last question, we already open and read the file, and split the 
# words into strings.

# create 2 counters up and lo.
# write a nested loop, the first layer for loop is looped by each word in stri.
# (the length of stri is 1000, range function will give a sequence for i from
# 0 to 999, and i is applied as the index of each word.)

# the first layer each time gives us a string of a single word
# the second layer's for loop looks at each letter within a given word string.
# if the letter within a word is a upper case letter, then up counter adds 1.
# if the letter within a word is a lower case letter, then lo counter adds i.

# print the results.

up =0
lo =0
# for i from 0 to 999
for i in range(len(stri)):
    word_i = stri[i]
    for j in word_i:
        if j.isupper():
            up += 1
        if j.islower():
            lo += 1

print("the amount of the uppercase letters is:", up)
print("the amount of the lowercase letters is:", lo)

    

    

