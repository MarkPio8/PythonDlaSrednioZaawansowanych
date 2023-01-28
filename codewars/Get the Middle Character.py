def get_middle(s):
    if len(s) % 2 == 0:
        return "{}{}".format(s[int((len(s)/2)-1)],s[int((len(s)/2))])
    else:
        return "{}".format(s[int((len(s)/2)+0.5-1)])
print(get_middle("testing"))