def check_type(typ, txt):
    res = ''
    if typ == "int":
        print(int(txt) * 2)
    elif typ == "real":
        print(f"{float(txt) * 1.5:.2f}")
    elif typ == "string":
        print(f"${txt}$")


type_ = input()
text = input()
check_type(type_, text)
