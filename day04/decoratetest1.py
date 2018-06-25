# -*- coding:utf-8 -*-
# Author:Yatces

user,pwd =  'yatces',"123456"

def timmer(auth_type):
    print("auth_type:",auth_type)
    def outer_warpper(func):
        def warpper(*args,**kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if auth_type == "local":
                if user == username and pwd == password:
                    print("successed!!")
                    res = func(*args,**kwargs)
                    return res
                else:
                    exit("error")
            else:
                print("no local")

        return warpper
    return outer_warpper


def index():
    print("this is index page")

@timmer(auth_type="local")
def home():
    print("my name is home page")
    return "home page"

@timmer(auth_type="file")
def bbs():
    print("begin to send bbs")

index()
print(home())
bbs()

