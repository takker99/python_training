# No.003
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import string

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = [len(i if i[-1] in string.ascii_letters else i[:-1]) for i in sentence.split()]
print(result)
