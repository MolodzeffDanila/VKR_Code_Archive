from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
from sklearn.model_selection import train_test_split

def mload_split():
    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5,random_state=42)
    return X_train[:15], y_train[:15]

student_answer = ""
correct_answer = ""

student_answer += str(load_split())
correct_answer += str(mload_split())
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_split. Тест №{}".format(1))
