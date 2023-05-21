from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.datasets import load_iris

X,y = load_iris(return_X_y=True)

min_max_scaler = preprocessing.StandardScaler()
scaled_data = min_max_scaler.fit_transform(X)

def mpredict_model(data):
    clustering = DBSCAN(eps=0.7, min_samples=2).fit(data)
    return set(clustering.labels_)

student_answer = ""
correct_answer = ""

student_answer += str(predict_model(scaled_data))
correct_answer += str(mpredict_model(scaled_data))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции predict_model. Тест №{}".format(1))
