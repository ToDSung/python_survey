class a(): 

    def __init__(self):
        print("親爸")


class b():

    def __init__(self):
        # 雖然 b 與 a 沒有關係 但 super 可以 呼叫 a 的 init
        super(b, self).__init__()
        print('後爸')

    def run(self):
        print('b的另一個方法')  

class c(b, a): 
    # 擺在前面的 class 優先繼承
    def __init__(self):
        super(c, self).__init__()
        print('兒子')
if __name__ == '__main__':
    c1 = c()
    c1.run() # 使用b的一个方法
    print(c.__mro__)
