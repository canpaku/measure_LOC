# -*- coding:utf-8 -*-

import re

class measure_loc:

    text = ""

    #未指定の場合"test.java"というファイル名のファイルを扱う
    def __init__(self, filename = "test.java"):
        self.filename = filename
        ff = open(filename)
        self.text = ff.read()
        ff.close()

    #ファイルを行ごとにリストに読み込む
    def get_textlines(self):
        f = open(self.filename)
        textlines = f.readlines()
        f.close()

        return textlines

    #行数を把握：total LOC
    def get_total_LOC(self):
        textlines = self.get_textlines()
        totalLOC = len(textlines)

        print(totalLOC)

    #空白の行数を把握
    def get_blank_LOC(self):
        textlines = self.get_textlines()
        blankLOC = 0

        for i in textlines:
            if i == "\n":
                blankLOC += 1

        print(blankLOC)

    #クラス数を数える
    def get_NOC(self):
        pattern = r" class "
        classnum = 0

        # パターンにマッチしたすべてをイテレータとして返す
        iterator = re.finditer(pattern, self.text)
        for match in iterator:
            classnum += 1

        print(classnum)

    #クラスごとのサイクロマティック数
    def get_cyclomatic_num(self):
        pattern = r" if "
        cyclonum = 0

        # パターンにマッチしたすべてをイテレータとして返す
        iterator = re.finditer(pattern, self.text)
        for match in iterator:
            cyclonum += 1

        print(cyclonum)


if __name__ == '__main__':

    result = measure_loc()
    result.get_total_LOC()
    result.get_blank_LOC()
    result.get_NOC()
    result.get_cyclomatic_num()

