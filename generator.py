# -*- coding: utf-8 -*-

"""
Created on Tue Oct  1 20:43:33 2024

@author: ASJ
"""

from random import randint
import pandas as pd


word_file = 'word.csv'
df = pd.read_csv(input1,index_col=0)

advs = df.loc['advs']

adjs = df.loc['adjs']

nouns = df.loc['nouns']

verbs = df.loc['verbs']

def get_adv():
    return advs[randint(0, len(advs) - 1)]


def get_adj():
    return adjs[randint(0, len(adjs) - 1)]


def get_noun():
    return nouns[randint(0, len(nouns) - 1)]


def get_verb():
    return verbs[randint(0, len(verbs) - 1)]


def get_title():
    return get_adv() + "后" + get_adj() + "的我和" + get_noun() + get_verb()


def main():
    print(get_title())


if __name__ == "__main__":
    main()
