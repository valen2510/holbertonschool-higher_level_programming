#!/usr/bin/pyhton3
def multiple_returns(sentence):
    if len(sentence) is 0:
        return(len(sentence), None)
    return(len(sentence), sentence[0])
