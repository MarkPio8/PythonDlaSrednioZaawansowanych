a = b = c = 10

print('Values a = %d, b = %d, c = %d' % (a,b,c))
print('ID id(a) = %s, id(b) = %s, id(c) = %s'%(id(a),id(b),id(c)))

a = 20

print('Values a = %d, b = %d, c = %d' % (a,b,c))
print('ID id(a) = %s, id(b) = %s, id(c) = %s'%(id(a),id(b),id(c)))

a = b = c = [1,2,3]

print('Values a =', a, ' b =', b, ' c =', c)
print('ID id(a) = %s, id(b) = %s, id(c) = %s'%(id(a),id(b),id(c)))

a.append(4)

print('Values a =',a,' b =',b,' c =',c)
print('ID id(a) = %s, id(b) = %s, id(c) = %s'%(id(a),id(b),id(c)))


x = 10
y = 10
print('Id id(x) = %s, id(y) = %s' %(id(x),id(y)))

y = y - 1  + 1
print('Id id(x) = %s, id(y) = %s' %(id(x),id(y)))

y = y - 1234567890  + 1234567890
print('Id id(x) = %s, id(y) = %s' %(id(x),id(y)))