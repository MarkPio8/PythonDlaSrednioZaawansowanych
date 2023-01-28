from bs4 import BeautifulSoup
import requests
import sys
from csv import writer

for i in range(0,4):
    url = "https://www.food.be/companies/search?search_api_fulltext=&page={}".format(i)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    lists = soup.find_all('div', class_="views-row")


    with open(r"C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\Other projects\food.csv",'a',encoding='utf8',newline='')as f:

        thewriter = writer(f)


        for list in lists:
            companyName = list.find('h3', class_ ="companies__item__title").text
            productType = list.find('div', class_ = "companies__item__categories").text.replace("\n","")

            link = list.find('div', class_ = 'companies__item__detail')
            link = str(link)

            start = link.find('href="')
            link = link[start+6:]

            end = link.find('"')
            link = link[:end]




            try:
                linkUnder = r"https://food.be{}".format(link)



                pageUnder = requests.get(linkUnder)

                soupUnder = BeautifulSoup(pageUnder.content, "html.parser")

                listsCompanySpecs = soupUnder.find('div', class_="company-specs")

                website = []
                find = []
                address = []
                street = []
                zipCodeCity = []
                i = 0
                c = 0
                tel = []
                mail = []
                name = []
                about = []
                brands = []

                # website
                for listUnder in listsCompanySpecs:
                    # i+=1
                    # print("{} = {}".format(i,listUnder))
                    # print("-"*30)

                    if str(listUnder).find('website') >= 0:
                        #     print(listUnder.text)
                        website.append(listUnder.text)

                listsContactInfo = soupUnder.find_all('div', class_="contact-info__section")
                try:
                    name.append(soupUnder.find('div', class_='field--name-field-company-contact').text + "~")
                except:
                    name.append("~")
                try:
                    about.append(format(soupUnder.find('div', class_='text-formatted').text+ "~"))
                except:
                    about.append("~")

                try:
                    brands.append(soupUnder.find('div', class_='table-scroll').text.replace("\n", " ") + "~")
                except:
                    brands.append("~")

                for listUnder in listsContactInfo:
                    # i+=1
                    # print("{} = {}".format(i,listUnder))
                    # print("-"*30)
                    if str(listUnder).find('maps') >= 0:
                        for list in listUnder:
                            if str(list).find('maps') >= 0:
                                for a in list:
                                    address.append(a.text)

                                    # street
                                    if c == 1:
                                        street.append(a.text + '~')

                                    # zipCodeCity
                                    elif c == 3:
                                        zipCodeCity.append(a.text + '~')
                                    c += 1
                            # tel

                            if str(list).find('tel') >= 0:
                                for a in list:
                                    tel.append(a.text + '~')
                            elif tel[0] != '~':
                                tel = tel
                            else:
                                tel.append('~')

                            # mail
                            if str(list).find('mail') >= 0:
                                for a in list:
                                    mail.append(a.text + '~')

                            elif mail[0] != '~':
                                mail = mail

                            else:
                                mail.append("~")

                website = str(website[0]) + '~'

                # print("zipCode City = {}".format(zipCodeCity))
                # print("street = {}".format(street))
                # print("website = {}".format(website))
                # print("tel = {}".format(tel))
                # print("mail = {}".format(mail))
                # print("name = {}".format(name))
                # print("about = {}".format(about))
                # print("brands = {}".format(brands))



                companyName += "~"
                productType += "~"
                info = [companyName, productType,zipCodeCity,street,website,tel,mail,name,brands]
                # info = [about]
                thewriter.writerow(info)
                for i in info:
                    i.replace('\t',' ')
                    # print(i)

                # thewriter.writerow(info)

            except:
                thewriter.writerow(sys.exc_info())



# print("find = {}".format(find))
