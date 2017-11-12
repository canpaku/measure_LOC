#coding: utf-8

class measure_loc:

    #未指定の場合"test.java"というファイル名のファイルを扱う
    def __init__(self, filename = "test.java"):
        self.filename = filename
        self.count_newline = 0

    #ファイルをリストに読み込む
    def get_textlines(self):
        f = open(self.filename)
        textlines = f.readlines()
        f.close()

        return textlines

    #行数を把握：total LOC
    def get_newlinenum(self):
        textlines = self.get_textlines()
        newlinenum = len(textlines)

        print(textlines)
        print(newlinenum)






if __name__ == '__main__':
    result = measure_loc()
    result.get_newlinenum()
