from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X,y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)

model = LinearRegression().fit(X_train, y_train)

def mpredict_model(model,X_test):
    y_pred = model.predict(X_test)
    return y_pred

student_answer = ""
correct_answer = ""

student_answer += str(predict_model(model,X_test))
correct_answer += str(mpredict_model(model,X_test))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции predict_model. Тест №{}".format(1))

