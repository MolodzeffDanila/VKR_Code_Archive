from sklearn.datasets import load_linnerud

def mload_data():
    X, Y = load_linnerud(return_X_y=True)
    return X, Y

student_answer = ""
correct_answer = ""

student_answer += str(load_data())
correct_answer += str(mload_data())
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_data. Тест №{}".format(1))

Проверка задачи “Преобразование данных к DataFrame.”:
from sklearn.datasets import load_linnerud
import pandas as pd

X, Y = load_linnerud(return_X_y=True)

def mcast_to_df(X, Y):
    dfX = pd.DataFrame(data=X, columns = ["Weight","Waist","Pulse"])
    dfY = pd.DataFrame(data=Y, columns = ["Pull-ups", "Squats","Jumps"])
    return dfX, dfY

student_answer = ""
correct_answer = ""

student_answer += str(mcast_to_df(X, Y))
correct_answer += str(mcast_to_df(X, Y))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_data. Тест №{}".format(1))
