import nlp_text
import pandas as pd
import numpy as np

print('')
print('')

tokens = nlp_text.preproc()
# print(tokens)

def exp_attr(x):
    lst , rlst =[] , []

    df=pd.read_csv("attributes.csv")
    lst = df.values

    for i in lst:
        if i[0] in x:
            rlst.append(i[1])

    if len(rlst) == 0:
        rlst.append('*')

    # print(rlst)
    return rlst


def imp_attr(x):
    lst , rlst = [] , []

    df=pd.read_csv("domain_dictionary.csv")
    lst = df.values

    for i in lst:
        if (i[0].lower()) in x:
            rlst.append(i[1])
            rlst.append(i[0])
    
    # print(rlst)
    return rlst


def gen_query(x):
    lst , slct , frm , wher = [] , [] , [] , []
    que = ""

    slct = exp_attr(x)
    wher = imp_attr(x)

    df=pd.read_csv("relations.csv")
    lst = df.values

    for i in lst:
        if (i[0] in slct and i[1] not in frm):
            frm.append(i[1])
        
        if (i[0] in wher and i[1] not in frm):
            frm.append(i[1])

    que += ("SELECT " + (','.join(slct)) + " FROM " + (','.join(frm)) + " WHERE ")
    
    j = 0
    while j < len(wher):
        que += wher[j] + '=' + "'" + wher[j+1] + "'" + ' AND '
        j += 2
    
    que = que.rstrip(' AND ')

    return que


print('')
print(gen_query(tokens))
print('')
print('')