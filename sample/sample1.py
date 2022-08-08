import random

# コメント
"""
複数行
コメントっぽいモノ
"""
date = str(2022) + "年" + str(8) + "月"
print(date)
# キーボード入力した値を取得
# input = input()
# print(input)

# 可変長配列
list_x = ["a", "b", "c", "d", "e"]
# マイナスのインデックスをつければ逆順で出力できる
print(list_x[-2])
print(len(list_x))

# ()で囲うかその()を省略してもよい
tuple = "a", "b", "c", "d", "e"
# タプルはイミュータブル
# tuple[3] = "x"

# in で中身と一致するかが取れる
print("c" in tuple)

if tuple[2] in("a", "b", "c"):
    print("a～c")
elif tuple[2] in("d", "e"):
    print("d～e")

# pythonではコレクションの類をシーケンス型と呼んでいる

# 同じ文字列ならば同じオブジェクトが割り当てられる
str1 = "あああ"
str2 = "あああ"
print(id(str1))
print(id(str2))
print(str1 == str2)
# 文字列スライス
str3 = "あいうえお"
print(str3[1:3])
print(str3.find("え"))

# 結果ナシや0をFalseのように扱える

for element in list_x:
    print(element)

for counter in range(10, 40, 8):
    print(counter)

# インデックスと要素を同時に取る
for index, element in enumerate(list_x):
    print(str(index) + "：" + element)

# 複数のコレクションをまとめてループ(回数は小さいほうに合わせる)
weekday1 = ["Sun", "Mon", "Tue"]
weekday2 = ["日", "月", "火", "水", "木", "金", "土", "日"]
for (eng, jp) in zip(weekday1, weekday2):
    print(eng + "：" + jp)
# for文でのelseブロックはループ完了時に実行される
else:
    print("ループ終了")

# 例外処理
try :
    9 / 0
except ZeroDivisionError :
    print("ゼロ除算です")

template ="{1} Hello, {0}"
print(template.format("Python", "Welcome"))

# リストは + で結合可能
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
for element in lst1 + lst2:
    print(element)
# リストは * で乗算可能
print(lst1 * 2)
# リストはスライス可能
print(weekday2[:3])
print(weekday2[2:])
print(weekday2[2:5])

# 要素の追加はappend
weekday1.append("Wed")
print(weekday1)

# 簡単にリダクション可能
print(sum(lst2))

# 集合(Set)は{}で囲う
set1 = {1, 4, 5, 3, 6, 3, 2, 2}
set1.add(7)
set1.add(1)
print(sorted(set1))

# Pythonの関数は先に定義しなければ呼び出せない
# print(add_function(10, 32))

# 引数にデフォルト値を持たせることもできる
def add_function(a, b = 10000):
    return a + b

print(add_function(10, 32))
print(add_function(111))

# キーワード引数による呼び出し(順番を入れ替えられる)
print(add_function(b = 32, a = 100))


def add_list(list):
    list.append("追加")

list_call = ["a", "b", "c"]
# ミュータブルなので引数で受けなくても良い
add_list(list_call)
print(list_call)

# アスタリスクを前につけると可変長引数として受け取れる
def add_function2(*elements):
    print(sum(elements))

add_function2(1, 2, 3, 4)

# アスタリスクを前に2つつけると連想配列として受け取れる
# 通常の引数の記述はできない
def dictionary_preview(**dictionary):
    print(dictionary)

dictionary_preview(name="Tanaka", age = 29)

# 変数に格納するときは()はつけない
my_func = dictionary_preview
my_func(aaa = "test")

# ラムダ式
smaller = lambda num1, num2 : "num2のが小さい" if num1 > num2 else "num1のが小さい"
print(smaller(11, 42))

# mapメソッドでラムダ式を渡してStream APIっぽいことが出来る
base_list = [1, 2, 3, 4, 5]
# listコンストラクタでmapの結果をリストに変換
new_list = list(map(lambda num : num * 2, base_list))
print(new_list)

# 内包表記
new_list2 = [n * 3 for n in base_list]
print(new_list2)

# filterメソッド
new_list3 = list(filter(lambda num : num % 2 == 0, base_list))
print(new_list3)

# 年齢でソート
names = {"Taro" : 33, "Makoto": 21, "Masato" : 43, "Hana" : 28}
for name in sorted(names.items(), key = lambda n : n[1]):
    print(name)

#ジェネレータ関数
def my_gen1(str) :
    for c in str.upper() :
        yield c

var1 = "hello"
gen = my_gen1(var1)
for c in range(len(var1)) :
    # nextで結果を取る
    print(next(gen))

def random_gen(num) :
    randoms = []

    while True :
        # 引数の値未満のランダムな値を生成
        rand_num = random.randrange(num)
        # 乱数に重複が無い場合
        if rand_num not in randoms :
            randoms.append(rand_num)
            yield rand_num
        # すべての乱数が生成された
        elif len(randoms) == num :
            break

ran_base = 10
rand = random_gen(ran_base)
for c in range(ran_base) :
    print(next(rand))

# ジェネレータ式
str_gen = "good"
gen1 = (c for c in str_gen.upper())
for char in gen1 :
    print(char)
