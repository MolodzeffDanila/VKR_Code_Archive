from sklearn import datasets

def mload_split():
    X, y = datasets.load_wine(return_X_y=True)
    return X, y

student_answer = ""
correct_answer = ""

student_answer += str(load_split())
correct_answer += str(mload_split())
if(student_answer != correct_answer):
    raise Exception("Ошибка в функции load_split. Тест №{}".format(1))
