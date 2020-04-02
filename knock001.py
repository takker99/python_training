# No.001
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

string = "パタトクカシーー"

# 内包表記
print(f"The result is {''.join([string[i-1]for i in [1,3,5,7]])}")

# slice 表記
print(f"The result is {string[::2]}")
