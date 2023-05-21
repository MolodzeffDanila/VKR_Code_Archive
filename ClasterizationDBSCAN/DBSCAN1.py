from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.datasets import load_iris

def mload_data():
    X,y = load_iris(return_X_y=True)
    min_max_scaler = preprocessing.StandardScaler()
    scaled_data = min_max_scaler.fit_transform(X)
    return scaled_data

student_answer = ""
correct_answer = ""

student_answer += str(load_data())
correct_answer += str(mload_data())
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции predict_model. Тест №{}".format(1))
