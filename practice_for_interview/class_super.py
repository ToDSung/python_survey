# class Base:
#     def __init__(self):
#         print('Base.__init__')

# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')

# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.__init__')

# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')

if __name__ == '__main__':
    # 使用 Base.__init__(self) 會兩次呼叫Base.__init__
    # 使用 super 可避免問題
    # 關鍵字 MRO
    # 注意多重繼承時是廣度搜尋
    
    # 子類會先於父類被檢查
    # 多個父類會根據它們在列表中的順序被檢查
    # 如果對下一個類存在兩個合法的選擇，選擇第一個父類
    c = C()