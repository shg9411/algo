import re

regex = re.compile(
    r'(?=.*[a-zA-Z])(?=.*\d)(?=.*[+=%_!@#$^&*?]).{8,}$', re.VERBOSE)


def checkPw():
    password = input("비밀번호를 입력하세요.\n")
    if regex.match(password):
        print("accepted")
    else:
        print("retry")
        checkPw()


checkPw()
