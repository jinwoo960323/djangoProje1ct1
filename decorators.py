def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def hello_world(input_text):

    print(input_text)



hello_world('hello_wolrd!')


def Square():
    a*b
    if request.user.is_authenticated and self.get_object() == request.user:
        return
    else:
        return Error