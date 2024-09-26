# @functools.wraps(func) 确保 wrapper 函数在替换 func 之前保留了 func 的元数据。
# 这样做使得即使 post_comment 被 authenticate 装饰后，
# 依然可以通过 post_comment.__name__ 获取到正确的函数名，
# 通过 post_comment.__doc__ 获取到正确的文档字符串等。

import functools
def check_user_logged_in(logged):
    return logged

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logged=args[0]

        if check_user_logged_in(logged):
            return func(*args,**kwargs)
        else:
            raise Exception("Not logged in")

    return wrapper

@authenticate
def post_comment(logged, comment):
    print("Posting comment: {}".format(comment))


post_comment(True,"hello,world")
print(post_comment.__name__)