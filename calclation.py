# systemname and version
print("EasyCalc v.1.0.0")



# 変数


index_numberList = ("0","1","2","3","4","5","6","7","8","9")
index_symbol = ("+","-","*","/","%","=")
commandList={"command":"!end !calclate !canI"
            ,"end":""
            ,"calclate":"+：和\n-：差\n/：商\n*：積\n%：余り\n"
            ,"canI":"和差商積と余りの計算ができます"}

index2d_memory = [[],[]]



# 初期表示文字

print("半角でかつ空白文字を入力しないでください")
print("!commandでコマンド一覧を閲覧できます。\nこの計算機のできることや四則演算その他計算のやり方を見ることができます\n")



# テキストの判別と出力
def textRead(calcText):
    if calcText[:1] == "!":
        return cmdRead(calcText)
    else :
        return calcRead(calcText)



# 命令:コマンド文章解析
def cmdRead(cmdText):
    
    cmdText = cmdText[1:]
    if cmdText in commandList:
        print(commandList[cmdText] + "\n")   # commandList辞書に登録した一覧から表示
    else:
        print("No Exit " + cmdText + " command")
        print("")
    
    if cmdText == "end":
        return 4
    
    return 0




# 命令:文章解析
def calcRead(calcText):

    symbols=[]
    numbers=[]
    numberCount = 1
    numberBegin = 0
    numberSum = 0
    #return 1:正常終了 2:異常終了
    
    
    for tex_char in calcText:   # ここでループで１文字ずつ文字を取り出す
        
        if (numberCount == 1 or numberBegin == numberCount-1) and index_numberList.count(tex_char) == 0:   # 数字以外の不正な記号の確認
            # print("異常終了:文章解析1")
            return 2
        elif index_symbol.count(tex_char) == 1: # 記号であれば
            symbols.append(tex_char) # 記号が何番目にあるか記録
            numbers.append(int(calcText[numberBegin:numberCount-1])) # n番目の数字を記録
            numberSum = calclator(numberSum,numbers[len(numbers)-1],symbols[len(symbols)-2],len(symbols))
            numberBegin = numberCount # 数字の始まりを記録
        elif index_numberList.count(tex_char) == 1: # 数字であれば
            pass
        else:
            # print("異常終了:文章解析2")
            return 2
        
        
        if tex_char == "=" and len(symbols) >= 2: # "="でかつ数字の始まりが1でない
            inMemory(calcText,numberSum)
            # print("正常終了:文章解析")
            return 1
        
        
        
        numberCount+=1
        
    # 1:正常終了 2:異常終了
    print("異常終了:文章解析3")
    return 2

# 命令:計算
def calclator(numberSum,numberElmnt,symbolElmnt,calcCount):
    if calcCount == 1: return numberElmnt
    elif symbolElmnt == "+": numberSum += numberElmnt
    elif symbolElmnt == "-": numberSum -= numberElmnt
    elif symbolElmnt == "*": numberSum *= numberElmnt
    elif symbolElmnt == "/": numberSum /= numberElmnt
    elif symbolElmnt == "%": numberSum %= numberElmnt
    elif symbolElmnt == "=": print("aaaaa")
    else: 
        print("致命的なエラーが発生しました、計算できません。(発生場所:calclator # 命令:計算)")
        return 0
    
    
    # print("正常終了:計算")
    return numberSum

# 命令:記憶入力
def inMemory(calcText,numberSum):
    
    index2d_memory[0].append(calcText)
    index2d_memory[1].append(numberSum)
    # print("正常終了:記憶")
    
    return 0

# 命令:記憶出力
def outMemory():
    
    print(index2d_memory[0][-1] + " " + str(index2d_memory[1][-1]))
    return 0



# 処理本文
while True:
    print("次のように記述してください: 123*456=")
    calcText = input(">>> ")
    
    
    # 0:コマンド 1:式 2:不正な文字列
    flg_tex = textRead(calcText)
    
    # 1:正常(計算可能),2:(計算不可)
    if flg_tex == 0:
        pass
    elif flg_tex == 1:
        outMemory()
    elif flg_tex == 2:
        print("正しく数字を入力してください")
    elif flg_tex == 4:
        print("プログラムを終了します")
        break
    



