import requests
import datetime
import xlsxwriter
import os

### config ###
URL = 'EXAMPLE URL'
PARAMS = {'KEY': 'VALUE'} 
filename = "TOPIC_"+datetime.date.today().strftime("%d_%B_%Y")

##############

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(os.path.abspath(os.getcwd())+'/'+filename+'.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

r = requests.get(url = URL, params = PARAMS)

header = tuple(r.json()[0].keys())
# print(header)

for i in header :
    if i != 'status' :
        worksheet.write(row, col, i)
        col+=1

row = 1
col = 0

for data in r.json() :
    col = 0
    for h in header :
        if h != 'status' :
            worksheet.write(row, col, str(data[h]).replace('\n',' '))
            col+=1
    row +=1
        

workbook.close()