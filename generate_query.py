import nlp_text
import pandas as pd
import numpy as np

print('')
print('')

tokens = nlp_text.preproc()
print(tokens)

def exp_attr(x):
    lst =[]
    str = ""

    df=pd.read_csv("attributes.csv")
    lst = df.values

    for i in lst:
        if i[0] in x:
            str += (i[1] + ',')
    
    str = str.rstrip(',')

    if str == "":
        str += '*'

    # print(str)
    return str

def imp_attr(x):
    lst =[]
    str = ""

    df=pd.read_csv("domain_dictionary.csv")
    lst = df.values

    for i in lst:
        if (i[0].lower()) in x:
            str += (i[1] + ' = ' + i[0] + " AND ")

    str = str.rstrip().rstrip('AND')
    
    # print(str)
    return str

print('')
print("SELECT " + exp_attr(tokens) + " WHERE " + imp_attr(tokens))
print('')
print('')