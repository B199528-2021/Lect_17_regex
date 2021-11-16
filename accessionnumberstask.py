#!/usr/local/bin/python3

import re

acclist = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

print("\nThis is the list:")
print(acclist)

print("\nContain number 5:")
for acclistitem in acclist:
    if re.search("5", acclistitem):
        print(acclistitem)

print("\nContain letter d or e:")
for acclistitem in acclist:
    if re.search("[de]", acclistitem):
        print(acclistitem)

print("\nContain letter d and e in that order:")
for acclistitem in acclist:
    if re.search("[de]", acclistitem):
        anyorder = acclistitem
        if anyorder.find("d") < anyorder.find("e"):
            print(anyorder)

print("\nContain letter d and e in that order with single letter between them:")
for acclistitem in acclist:
    if re.search("d.e", acclistitem):
        print(acclistitem)

print("\nContain both the letters d and e in any order:")
for acclistitem in acclist:
    if re.search("d", acclistitem) and re.search("e", acclistitem):
        print(acclistitem)

print("\nStart with x or y:")
for acclistitem in acclist:
    if re.search("^[xy]", acclistitem):
        print(acclistitem)

print("\nStart with x or y and end with e:")
for acclistitem in acclist:
    if re.search("^[xy]", acclistitem) and re.search("e$", acclistitem):
        print(acclistitem)

print("\nTest: Contain numbers in general:")
for acclistitem in acclist:
    if re.search(r"\d+", acclistitem):
        print(acclistitem)

print("\nTest: Print numbers only (print them as strings):")
for acclistitem in acclist:
    # get the numbers of the items
    print(re.search(r"\d+", acclistitem).group())

print("\nContain any 3 numbers in any order:")
for acclistitem in acclist:
    # get the numbers of the items
    if len(re.search(r"\d+", acclistitem).group()) > 2:
        print(acclistitem)

print("\nContain any 3 numbers in any order:")
for acclistitem in acclist:
    # get the numbers of the items
    if len(re.search(r"\d+", acclistitem).group()) == 3:
        print(acclistitem)










