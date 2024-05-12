# cook your dish here
def str_title(s):
    words = s.split()
    title = []
    for i in words:
        if i.isupper():
            title.append(i)
        else:
            title.append(i.title())
    return ' '.join(title)

t = int(input())
while t>0:
    s=input()
    print(str_title(s))
    t-=1
