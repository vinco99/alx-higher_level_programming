#!/usr/bin/python3

def multiple_returns(sentence):
    slen = len(sentence)
    if slen == 0:
        res = (0, None)
        return res
    else:
        result = (slen, sentence[0:1])
        return result
