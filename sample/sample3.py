
# ファイルをオープンする
from math import e


try : 
    f = open("input.txt", "r", encoding="utf_8")
    # ファイルを読み込む
    lines = f.read(2)
    print(lines)
    lines = f.read(4)
    print(lines)

    # 各行をリストにする
    lines2 = f.readlines()
    for i, line in enumerate(lines2) :
        print("{:3d}:{}".format(i,line.rstrip("\n")))

    # ファイルをクローズする
    f.close
except FileNotFoundError as e:
    print("ファイルないよ", e)
finally :
    print("おわり")


try : 
    f = open("input.txt", "r", encoding="utf_8")
    i = 0
    while True :
        # 1行ずつ読み込む
        line = f.readline()
        if line == "" :
            break
        print("{:3d}:{}".format(i,line.rstrip("\n")))
        i +=1
    f.close
except FileNotFoundError as e:
    print("ファイルないよ", e)
finally :
    print("おわり")

# 直接イテレートすることもできる
try : 
    f = open("input.txt", "r", encoding="utf_8")
    for i, line in enumerate(f) :
        print("{:3d}:{}".format(i,line.rstrip("\n")))

    f.close
except FileNotFoundError as e:
    print("ファイルないよ", e)
finally :
    print("おわり")


# with文でtry-catch-resourcesっぽいことができる
# close忘れが無いのでこっち使った方がいいね
try : 
    with open("input.txt", "r", encoding="utf_8") as f :
        for i,line in enumerate(f) :
            print("{:3d}:{}".format(i,line.rstrip("\n")))
except FileNotFoundError as e:
    print("ファイルないよ", e)
finally :
    print("おわり")