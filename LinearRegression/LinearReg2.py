from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split

X,y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)

def muniform(X_train,y_train):
    model = LinearRegression().fit(X_train, y_train)
    return model.coef_

student_answer = ""
correct_answer = ""

student_answer += str(uniform(X_train,y_train))
correct_answer += str(muniform(X_train,y_train))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции uniform. Тест №{}".format(1))
