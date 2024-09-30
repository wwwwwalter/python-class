def outdef():
    def indef():
        print('in def')

    # indef() #局部函数只在函数内

    return indef # 扩大局部函数作用域

new_indef = outdef()
new_indef()