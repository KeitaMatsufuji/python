
try : 
    # ファイルが無ければ作り、あっても上書きされる
    with open("output.txt", "w", encoding="utf_8") as f :
        f.write("どうも\n")
        f.write("こんにちは\n")

    # ファイルが無ければ作り、あれば追加される
    with open("output2.txt", "a", encoding="utf_8") as f :
        f.write("どうも\n")
        f.write("こんにちは\n")
    
    weekdays = ["月\n","火\n","水\n","木\n","金\n","土\n","日\n",]
    with open("days.txt", "w", encoding="utf_8") as f :
        # まとめて書き出す
        f.writelines(weekdays)
except FileNotFoundError as e:
    print("ファイルないよ", e)
finally :
    print("おわり")