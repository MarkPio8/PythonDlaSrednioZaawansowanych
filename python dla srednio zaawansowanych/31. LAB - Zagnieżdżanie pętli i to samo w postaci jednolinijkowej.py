ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))

# krk = 'krk'
# waw = 'lrk'
# krk = 'lrk'
# # krk = "KRK"
# # waw = "WAW"
#
# print(krk<waw)
# print(id(krk))
# print(id(waw))
