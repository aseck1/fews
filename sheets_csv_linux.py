# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:46:02 2017

@author: Yaayu_Sulay
"""
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

t0 = time.time()


directory1= "/home/user1/MODEL/p52fc04_sa/output/icprb/archived_precip/"
precip_file = "MARFC_PRC.csv"
f1 = os.path.join(directory1,precip_file)
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("marfc_precip_test").sheet1
 
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)

fi = open(f1)

row = 1
column = 1

for li in fi:
    items = li.strip().split(',')
    #print items
    for item in items:
        #print item
        column += 1
        sheet.update_cell(row, column, item)
	       
    row += 1
    column = 1
        
	       

#worksheet.update_cells(cell_list)

fi.close()

print(list_of_hashes)

t1 = time.time()

total = t1-t0

print "finished in how many seconds?"
print total