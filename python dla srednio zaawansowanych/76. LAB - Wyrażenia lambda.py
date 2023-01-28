text_list = ['x','xxx','xxxxx','xxxxxxx','']
f = lambda x : len(x)
print(f("abc"))
for a in text_list:
    print(f(a))

print(list(map(f,text_list)))
print(list(map(lambda x : len(x),text_list)))