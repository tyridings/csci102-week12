# Ty Ridings
# CSCI 102 - Section C
# Week 12 - Part A

def PrintOutput(word):
    print('OUTPUT', word)

def LoadFile(filename):
    with open(filename,'r+') as f:
        lines = f.readlines()
    print(lines)

def UpdateString(string1, string2, num):
    list1 = []
    final = ''
    for i in string1:
        list1 += i
    list1[num] = string2
    for n in list1:
        final += n
    print(final)
