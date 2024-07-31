class Test:

    def __init__(self, foo, newValue): # 特殊函数
        self.__foo = foo
        self.newValeLength = len(newValue)

    def __bar__(self): # 私有方法
        print(self.__foo)
        print('__bar:', self.newValeLength)

    def __bar(self): # 私有方法
        print(self.__foo)
        print('__bar:', self.newValeLength)

    def _bar(self): # 受保护方法
        print(self.__foo)
        print('__bar:', self.newValeLength)

    def bar(self):  # 公共函数 类的外部直接调用，用于执行类的公共行为
        print(self.__foo)
        print('__bar:', self.newValeLength)

    def __str__(self):
        return 'Test: [foo=%s]' % (self.foo)

    def __del__(self):
        print("销毁Class")


def main():
    test = Test('hello', "sssssssss2111111111111111111111")
    # test._Test__bar()
    # test.__bar() # 错误
    test.bar()
    test._bar()
    print(test.newValeLength)


if __name__ == "__main__":
    main()
