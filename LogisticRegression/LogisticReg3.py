from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8, random_state=42)
model = LogisticRegression(random_state=42).fit(X_train, y_train)

def mmodel_predict(X_test, model):
    y_pred = model.predict(X_test)
    return y_pred[:15]

student_answer = ""
correct_answer = ""

student_answer += str(model_predict(X_test, model))
correct_answer += str(mmodel_predict(X_test, model))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции model_predict. Тест №{}".format(1))
