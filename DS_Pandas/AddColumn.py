from sklearn.datasets import load_linnerud
import pandas as pd
import numpy as np

X, Y = load_linnerud(return_X_y=True)
dfX = pd.DataFrame(data=X, columns = ["Weight","Waist","Pulse"])
dfY = pd.DataFrame(data=Y, columns = ["Pull-ups", "Squats","Jumps"])
df = pd.concat([dfX, dfY], axis = 1)

def madd_col(df_):
    df_["ILoveCats"] = np.random.sample(df_.iloc[:,0].shape[0])
    return df_.columns

student_answer = ""
correct_answer = ""

student_answer += str(add_col(df))
correct_answer += str(madd_col(df))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции add_col. Тест №{}".format(1))
