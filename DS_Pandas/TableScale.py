import pandas as pd
import numpy as np

data =( (-1)) * np.random.sample((40,10)) + 0.8

df = pd.DataFrame(data=data)

df.iloc[1,2] = ''
df.iloc[1,3] = ''
df.iloc[1,5] = ''
df.iloc[2,2] = ''
df.iloc[7,2] = ''
df.iloc[7,3] = ''
df.iloc[10,2] = ''
df.iloc[12,8] = ''

def mdropempty(df_):
    for col in df_.columns:
        df_[col].replace('', np.nan, inplace=True)

    df_= df.dropna()
    df_ = df_.reset_index()
    return df_

student_answer = ""
correct_answer = ""

student_answer += str(dropempty(df))
correct_answer += str(mdropempty(df))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции dropempty. Тест№{}".format(1))
