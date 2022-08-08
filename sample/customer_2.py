from customer_1 import Customer
from datetime import date

class GoldCustomer(Customer) :
    # クラス変数(static)
    bmi = 22

    # コンストラクタ
    # アンスコが2つずつついたメソッドは特殊メソッドと呼ばれている
    def __init__(self, number, name, birthdate, height = 0) :
        # 前アンスコ2つでprivateになる
        self.__birthdate = birthdate
        super().__init__(number, name, height)

    def get_birthdate(selt) :
        return selt.__birthdate
    birthdate = property(get_birthdate)

# テスト用ブロック
if __name__ == "__main__" :
    taro = Customer(111, "テスト太郎", 200)
    print("{}標準体重:{:2f}kg".format(taro.get_name(), taro.std_weight()))
