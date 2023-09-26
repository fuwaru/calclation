#systemname and version
print("EasyCalc v.1.0.0")

#変数
dict_command ={}
dict.update({"command":"!end !calclate !canI"
            ,"end":"プログラムを終了します"
            ,"calclate":"+：和\n-：差\n/：商\n*：積\n%：余り\n"
            ,"canI":"和差商積と余りの計算ができます"})

flg_End = False

#初期表示文字
print("次のように記述してください: 123*456=")
print("また、半角でかつ空白文字を入力しないでください")
print("\n !commandでコマンド一覧を閲覧できます。\nこの計算機のできることや四則演算その他計算のやり方を見ることができます")



#テキストの種類
def reading_function(text_calc):
    if(text_calc == "!end"):
        return 1
    elif(text_calc == "123"):
        return 0
    else:
        print("不正な文字列です")
        return 2
    

#命令:コマンド
def command():
    print("coming soon...")

#命令:計算処理
def calclator():
    print("coming soon...")

#処理本文
while True:
    text_calc = input(">>> ")
    
    # "!"が最初についているテキストの判別
    test = reading_function(text_calc)
    print(test)
    break



