#!/usr/bin/python3
def multiple_returns(sentence):

    len_sen = len(sentence)

    if len_sen == 0:
        return None, None

    return (len_sen, sentence[0])
