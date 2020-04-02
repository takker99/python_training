# No.006
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
import ngram

sentence = ["paraparaparadise", "paragraph"]

X = set(ngram.n_gram(sentence[0], 2))
Y = set(gram.n_gram(sentence[1], 2))
print(f"X = {X}")
print(f"Y = {Y}")
print(f"X ∪ Y ={X+Y}")

print(f"X x Y =")
print(f"the letter bi-gram is {ngram.n_gram(sentence,2)}")
