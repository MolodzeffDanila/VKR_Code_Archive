from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8, random_state=42)
model = LogisticRegression(random_state=42).fit(X_train, y_train)
y_pred = model.predict(X_test)

def maccuracy(y_test,y_pred):
    return accuracy_score(y_pred,y_test)

student_answer = ""
correct_answer = ""

student_answer += str(accuracy(y_test,y_pred))
correct_answer += str(maccuracy(y_test,y_pred))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции accuracy. Тест №{}".format(1))
