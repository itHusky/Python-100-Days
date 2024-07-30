"""
学生考试成绩表
"""
import copy

def main():
    # names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    names = ['关羽', '张飞',]
    subjs = ['语文', '数学', '英语']
    # 初始化scores，确保每行都是一个独立的列表
    # TODO 使用了列表乘法来创建scores，这会导致所有行都引用同一个内部列表的多个副本。因此，当你修改任何一行的任何元素时，这个修改会反映在所有行上（因为所有行实际上都是同一个列表的引用）。
    # scores = [[0] * (len(subjs) + 1)] * len(names)
    scores = [[None] * (len(subjs) + 1) for _ in range(len(names))]
    for row, name in enumerate(names):
        print('请输入%s的成绩' % (name))
        scores[row][0] = name
        print(scores[row][0], row)
        for col, subj in enumerate(subjs):
            scores[row][col + 1] = float(input(subj + ': '))
    print(scores)

if __name__ == '__main__':
    main()
