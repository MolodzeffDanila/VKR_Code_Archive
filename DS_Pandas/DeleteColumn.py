from sklearn.datasets import load_linnerud
import pandas as pd

X, Y = load_linnerud(return_X_y=True)
dfX = pd.DataFrame(data=X, columns = ["Weight","Waist","Pulse"])
dfY = pd.DataFrame(data=Y, columns = ["Pull-ups", "Squats","Jumps"])
df = pd.concat([dfX, dfY], axis = 1)

def mdel_col(df_):
    df_.drop(columns = ['Waist'],axis = 1)
    return df_.columns

student_answer = ""
correct_answer = ""

student_answer += str(del_col(df))
correct_answer += str(mdel_col(df))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции del_col. Тест №{}".format(1))
