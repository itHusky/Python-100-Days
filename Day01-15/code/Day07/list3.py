"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

元组解包
解包时，左侧变量的数量必须与元组中元素的数量完全匹配，否则会引发ValueError。
如果只是想获取元组中的部分元素，可以在左侧使用*来捕获剩余的元素，但这需要Python 3.x的支持。

data = (1, 2, 3, 4, 5)
a, *rest = data
print(a)  # 输出: 1
print(rest)  # 输出: [2, 3, 4, 5]


"""


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1 # 元组解包
    # 等价于
    # a = 0
    # b = 1
    # 等价于
    # a,b = (0, 1)
    for _ in range(n):
        a, b = b, a + b # 元组解包
        # 等价于
        # new_a = b (原)
        # new_b = a (原) + b (原)
        # a = new_a, b = new_b
        # 等价于
        # a,b = (b, a + b)
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表达式
    list2 = [2*x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))
    # 生成器(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print("gen:", gen)
    for elem in gen:
        print(elem, end=',')
    print()
    gen = fib(20)
    print("fib:", gen)
    for elem in gen:
        print(elem, end=' ')
    print()


if __name__ == '__main__':
    main()
