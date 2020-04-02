# No.002
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

string1 = "パトカー"
string2 = "タクシー"

print(f"The result is {''.join([string1[i]+string2[i] for i in range( len(string1) )])}")
