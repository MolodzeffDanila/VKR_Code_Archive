from sklearn.datasets import load_linnerud
import pandas as pd

X, Y = load_linnerud(return_X_y=True)

dfX = pd.DataFrame(data=X, columns = ["Weight","Waist","Pulse"])
dfY = pd.DataFrame(data=Y, columns = ["Pull-ups", "Squats","Jumps"])

def mcorrelation(dfX, dfY):
    df = pd.concat([dfX, dfY], axis = 1)
    corrMatrix = df.corr()
    return corrMatrix

student_answer = ""
correct_answer = ""

student_answer += str(correlation(dfX, dfY))
correct_answer += str(mcorrelation(dfX, dfY))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции correlation. Тест №{}".format(1))
