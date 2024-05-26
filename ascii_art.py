# ascii_art.py
from art import *

def main():
    # 打印一个简单的艺术字
    print(art("hello"))

    # 打印随机艺术字
    print(art("random"))

    # 打印特定风格的艺术字
    print(text2art("Python", font='block'))

    # 打印 3D 风格的艺术字
    print(text2art("GitHub", font='block', chr_ignore=True))

    # 打印一个随机的艺术图形
    print(randomart())

    # 打印一个特定的艺术图形
    print(art("butterfly"))

if __name__ == "__main__":
    main()