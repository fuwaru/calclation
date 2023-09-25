#systemname and version
print("EasyCalc v.1.0.0")

#変数
flg_End = False

#初期表示文字
print("次のように記述してください: 123*456=")
print("また、半角でかつ空白文字を入力しないでください")
print("\n !commandでコマンド一覧を閲覧できます。\nこの計算機のできることや四則演算その他計算のやり方を見ることができます")


def calclator(text_calc):
    if(text_calc == "!end"):
        return 1
    elif(text_calc == "123"):
        return 0
    else:
        print("不正な文字列です")
    

#処理本文
while True:
    text_calc = input(">>> ")
    
    # "!"が最初についているテキストの判別
    test = calclator(text_calc)
    print(test)
    break


