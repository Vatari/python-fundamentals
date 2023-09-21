title = input()
comment = input()
content = input()
contents = []

while content != "end of comments":
    contents.append(content)
    content = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {comment}\n</article>")
for c in contents:
    print(f"<div>\n    {c}\n</div>")
