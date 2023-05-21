from sklearn.cluster import KMeans
from sklearn import datasets

X, y = datasets.load_wine(return_X_y=True)

def mpredict_model(X, y):
    k_means = KMeans(n_clusters=3,random_state=42, n_init="auto").fit(X)
    k_means_cluster_centers = k_means.cluster_centers_
    return k_means_cluster_centers

student_answer = ""
correct_answer = ""

student_answer += str(predict_model(X, y))
correct_answer += str(mpredict_model(X, y))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции predict_model. Тест №{}".format(1))
