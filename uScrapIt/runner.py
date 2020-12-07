import json 
import urllib3
import pandas as pd
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter

make = 'SUBARU'
model = 'IMPREZA'
year = '2017'

URL = "https://www.upullitne.com/search-inventory/"
req = urllib3.PoolManager()
res = req.request('GET', URL)
soup = BeautifulSoup(res.data, 'html.parser')
htmls = soup.prettify()
table = soup.find("table", { "class" : "footable-header" })

headers = ["Make","Model","Year","Color","STOCK_NUM","row","Location","date"]
tables =  list(list(soup.children)[2])[3]
table2 = list(list(tables)[3])
table3 = list(table2)[9]
TBC = list(list(list(table3)[3])[1])[1].find('tbody').contents

TBC_Clean = TBC[1::2]
cars = []
cols = []

for item in TBC_Clean:
    if make in item.find('td'):
        for i in item:
            #print(i)
            if model in i:
                print(model+"\n\n")
                cars += item
    
    #cars += item

# data = []
# for element in TBC_Clean:
#     sub_data = []
#     for sub_element in element:
#         try:
#             sub_data.append(sub_element.get_text())
#         except:
#             continue
#     data.append(sub_data)
for num, name in enumerate(cars,start=1):
    print("Column   ():".format(num,name))


df = pd.DataFrame(data =  columns=headers)
df.to_csv('csv.test.csv')