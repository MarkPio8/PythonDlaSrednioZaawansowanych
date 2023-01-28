import  os
import urllib.request
import sys

data_dir = r'/TEMP'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    try:
        print("processing "+page['name'])
        filename = page['name']+".html"
        path = os.path.join(data_dir,filename)
        urllib.request.urlretrieve(page['url'],path)
    except:
        print('ERROR>',sys.exc_info()[0])
        break
else:
    print("We got it all sites got installed")

# import urllib.request
# import os
#
# data_dir = r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP'
# pages = [
#     {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
#     {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
#     {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]
#
# for page in pages:
#
#     try:
#         file_name = "{}.html".format(page["name"])
#         path = os.path.join(data_dir, file_name)
#
#         print("Processing: {}  => {} ...".format(page["url"], file_name))
#         urllib.request.urlretrieve(page["url"], path)
#         print('...done')
#
#     except:
#         print('FAILURE processing web page: {}'.format(page["name"]))
#         print('Stopping the process!')
#         break
#
# else:
#     print('All pages downloaded successfully!!!')
