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

def FindWordCount(a_list, a_string):
    count = 0
    for i in a_list:
        if i == a_string:
            count += 1
    print('OUTPUT',count)

def ScoreFinder(str_list,float_list, name):
    f = 0
    for i in range(len(str_list)):
        if str_list[i].lower() == name.lower():
            print('OUTPUT %s got a score of %d' % (str_list[i],float_list[i]))
            f = 1
    if f == 0:
        print('player not found')
            
