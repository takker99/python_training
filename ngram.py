def n_gram(text: str, n: int):
    return [text[i : i + n] for i in range(len(text) - n + 1)]


if __name__ == "__main__":
    string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    for i in range(1, 5+1):
        print(f"n = {i} then {n_gram(string,i)}")
