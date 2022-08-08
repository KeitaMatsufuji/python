class Customer :
    # クラス変数(static)
    bmi = 22

    # コンストラクタ
    # アンスコが2つずつついたメソッドは特殊メソッドと呼ばれている
    def __init__(self, number, name, height = 0) :
        # 前アンスコ2つでprivateになる
        self.__number = number
        self.__name = name
        self.__height = height
    
    def std_weight(self) :
        return self.bmi * (self.__height / 100)** 2

    def get_number(selt) :
        return selt.__number

    def get_name(selt) :
        return selt.__name

    def get_heighte(selt) :
        return selt.__height

# テスト用ブロック
if __name__ == "__main__" :
    taro = Customer(111, "テスト太郎", 200)
    print("{}標準体重:{:2f}kg".format(taro.get_name(), taro.std_weight()))
