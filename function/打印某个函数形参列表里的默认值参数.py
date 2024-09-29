def dis_str(str1,str2 = "python2",str3 = "python3"):
    print("str1:",str1)
    print("str2:",str2)
    print("str3:",str3)


if __name__ == "__main__":
    print(dis_str.__defaults__) # 打印一个元组出来

    dirs = dis_str.__dir__()
    for name in dirs:
        print(name)
