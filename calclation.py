# systemname and version
print("EasyCalc v.1.0.0")



# 変数
flg_End = False
number_all = ("1","2","3","4","5","6","7","8","9")

dict_command={}
dict.update({"command":"!end !calclate !canI"
            ,"end":"プログラムを終了します"
            ,"calclate":"+：和\n-：差\n/：商\n*：積\n%：余り\n"
            ,"canI":"和差商積と余りの計算ができます"})



# 初期表示文字
print("次のように記述してください: 123*456=")
print("また、半角でかつ空白文字を入力しないでください")
print("\n !commandでコマンド一覧を閲覧できます。\nこの計算機のできることや四則演算その他計算のやり方を見ることができます")



# テキストの種類
def reading_function(text_calc):
    if text_calc[:1] == "!":
        command(text_calc)
    elif text_calc == "123":
        return 0
    else:
        print("不正な文字列です")
        return 2
    

# 命令:コマンド
def command(commands):
    print("coming soon...")
    text_commands = commands[2:]
    print(dict_command[text_commands] + "\n")   # dict_command辞書に登録した一覧から表示
    return 0




# 命令:計算処理
def calclator(tex_calc):
    print("coming soon...")
    symbol=[]
    number=[]
    flg_number = 1

    for tex_char in tex_calc:
        if flg_number == 1 and not tex_char in ["1","2","3","4","5","6","7","8","9"]:   # 最初に不正な文字がないか確認
            break
        
        if tex_char == "*" or "-" or "+" or "/" or "%" or "=":
            symbol.append(flg_number)
        
        if tex_char == "=":
            break
        
        flg_number+=1




# 処理本文
while True:
    text_calc = input(">>> ")
    
    
    test = reading_function(text_calc)  # "!"が最初についているテキストの判別
    print(test)
    break



