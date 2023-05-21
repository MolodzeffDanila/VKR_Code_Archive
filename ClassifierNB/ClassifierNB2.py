from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5,random_state=42)

def muniform(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    return gnb.score(X_test, y_test)

student_answer = ""
correct_answer = ""

student_answer += str(uniform(X_train, X_test, y_train, y_test))
correct_answer += str(muniform(X_train, X_test, y_train, y_test))
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_split. Тест №{}".format(1))
