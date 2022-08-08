from datetime import date
from customer_1 import Customer

# インスタンス生成
taro = Customer(101, "山田太郎", 180)
# インスタンスフィールドを追加
taro.birthdate = date(1992, 12, 3)
print(taro.std_weight())
print(taro.birthdate)

# staticフィールドを追加
Customer.LIMIT = 50

