#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substring_l = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    anagram_count = 0
    anagram_list = []
    for i in range(0,len(substring_l)):
        s1 = substring_l[i]
        for j in range(i+1, len(substring_l)):
            s2 = substring_l[j]
            if sorted(s1) == sorted(s2):
                anagram_list.append((s1,s2))
                anagram_count += 1
    print(anagram_list)
    return anagram_count

def sherlockAndAnagrams(s):
    # get the substring of s
    #substring_l = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    anagram_count = 0

    for i in range(0,len(s)-1):
        for j in range(i+1, len(s)):
            s1 = s[i:j]
            s1_l = j-i
            print("sl_len:",s1_l)
            for k in range(i+1, len(s) -s1_l+1):
                s2 = s[k:k+s1_l]
                print(s2)
                if sorted(s1) == sorted(s2):
                    anagram_count += 1
    return anagram_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()

