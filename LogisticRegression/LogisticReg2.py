from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8, random_state=42)

def mtrain_model(X_train,y_train):
    model = LogisticRegression(random_state=42).fit(X_train, y_train)
    return model.coef_

student_answer = ""
correct_answer = ""

student_answer += str(train_model(X_train,y_train))
correct_answer += str(mtrain_model(X_train,y_train))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции train_model. Тест №{}".format(1))
