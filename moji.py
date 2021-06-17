from PIL import Image
import sys
import pyocr
import pyocr.builders

def moji(a):
    #Available symbols
    symbols = ['-', ',', '?', '!']

    tools = pyocr.get_available_tools()
    tool = tools[0]

    langs = tool.get_available_languages()
    lang = langs[0]
    #txtに変換した文字列を代入する
    txt = tool.image_to_string(
        Image.open(a + '.png'),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    Text = list(txt)   #文字列を配列に変換
    count = len(Text)
    i = 0
    while True:   #寿司打の場合小文字アルファベットか'-'しか出てこないのでそれ以外の文字が出てきていたら削除する
        if i >= count:
            break
        if Text[i] < 'a' or Text[i] > 'z':
            if Text[i] not in symbols:
                del Text[i]
                count -= 1
            else:
                i += 1
        else:
            i += 1

    txt = str(''.join(Text))   #文字列に戻す
    return txt