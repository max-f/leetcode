#!/usr/bin/env python

# My Solution to https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = int("0b" + a, 2)
        b_dec = int("0b" + b, 2)
        c = a_dec + b_dec
        return str(bin(c))[2:]
