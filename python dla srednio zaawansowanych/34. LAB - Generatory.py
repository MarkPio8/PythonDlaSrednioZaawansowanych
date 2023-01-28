ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
size = 0
for i in routes:
    print(i)
    size +=1
print(size)

routes = ((start, stop) for start in ports for stop in ports if start != stop)
print(routes)
size = 0
for i in routes:
    print(i)
    size +=1
print(size)

routes = ((start, stop) for start in ports for stop in ports if start < stop)
print(routes)
size = 0
for i in routes:
    print(i)
    size +=1
print(size)