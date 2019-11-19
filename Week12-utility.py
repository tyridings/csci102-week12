# Ty Ridings
# CSCI 102 - Section C
# Week 12 - Part A

def PrintOutput(word):
    print('OUTPUT', word)

def LoadFile(filename):
    with open(filename,'r+') as f:
        lines = f.readlines()
    print(lines)
