import pandas as pd
import numpy as np
def total(k):
    lst = []
    for i in df.index:
        for j in df.columns:
            lst.append(df.loc[i,j])
    s = 0
    for i in lst:
        if type(i)==np.int64 or type(i)==np.float64:
            s +=i
    return s

df = pd.DataFrame({
    'person': ['Мария','Дмитрий','Александр','Пётр'],
    'salary':[50000,100000,20000,30000],
    'bonus':[2500.50,5000.70,1000.80,1500.90]
})

print(total(df))












