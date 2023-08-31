def progress_bar(bar):
    if bar == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{bar}% [{'%' * (bar // 10)}{'.' * (10 - bar // 10)}]\nStill loading..."


loading_bar = int(input())
print(progress_bar(loading_bar))
