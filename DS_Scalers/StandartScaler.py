from sklearn import preprocessing
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd

X, Y = load_iris(return_X_y=True)

def muniform(X, Y):
    scaler = preprocessing.StandardScaler().fit(X)
    data_scaled = scaler.transform(X)
    
    mean_scaled=data_scaled.mean(dtype=np.float32)
    std_scaled=data_scaled.std(dtype=np.float32)
    
    return round(mean_scaled,3), round(std_scaled,3)

student_answer = ""
correct_answer = ""

student_answer += str(uniform(X, Y))
correct_answer += str(muniform(X, Y))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_split. Тест №{}".format(1))
