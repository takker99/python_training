# No.005
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import ngram

sentence = "I am an NLPer"

print(f"the word bi-gram is {ngram.n_gram_word(sentence,2)}")
print(f"the letter bi-gram is {ngram.n_gram(sentence,2)}")
