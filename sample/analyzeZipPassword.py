import string,itertools,zipfile
 
def analizePassword(chars, file_path, size):
    count = 0
    analized = False
    result = ""
    # 総当たりの組み合わせでパスワードを検証
    for ch in itertools.product(chars, repeat=size):
        password = ''.join(ch)
        print(password)
        # 文字列型パスワードをバイト型に
        pwd = bytes(''.join(ch),'UTF-8')
        with zipfile.ZipFile(file_path , 'r') as zf:
            try:
                zf.extractall(path='.', pwd=pwd)
                print('success : password  : {}'.format(pwd))
                result = format(pwd)
                analized = True
                break
            except Exception as e:
                count +=1
    if not analized:
        # 桁を上げて再度総当たり
        size += 1
        analizePassword(chars, file_path, size)
    return result


chars = string.ascii_letters + string.digits
file_path = 'XXXX研修報告書yyyymmdd(なまえ).zip'
size = 1
print(analizePassword(chars, file_path, size))
 

