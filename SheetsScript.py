import math
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *
from math import ceil
import string
import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime
import time as td
import pytz

pytrend = TrendReq()

letters = string.ascii_uppercase

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("DataStorage").sheet1


# pprint(data)

# sheet.update("a1", "TGest Date")

def multirowtest():
    count = 2
    value = 2
    cell = None
    for i in range(0, 10):
        cell = "F" + str(count)
        sheet.update(cell, value)
        value = value ** 2
        count += 1


fmt = cellFormat(backgroundColor=color(0, 1, 0),)


# format_cell_range(sheet, 'A1:J1', fmt)
# set_column_width(sheet, "D", 20)


def makesheetsCircle():
    widthIdx = 6
    for i in range(0, 9):
        char = chars[widthIdx]
        set_column_width(sheet, char, 20)
        widthIdx += 1
    fomt = cellFormat(backgroundColor=color(0, 1, 0), )
    format_cell_ranges(sheet, [("I2:M11", fomt), ("H3:N10", fomt), ("G4:O9", fomt)])

# .cell(row, col).value outputs string
# .row_values(num) & .col_values(num) outputs list of strings


def find_row_end(end_num):
    set_num = ceil(end_num/26)
    location = end_num - ((set_num - 1) * 26)
    letter = letters[location-1]
    return set_num, letter


def is_empty(location, typ):
    if typ == "CEL":
        val = sheet.cell(location[0], location[1]).value
        if val == '':
            return True
        else:
            return False
    elif typ == "COL":
        val = sheet.col_values(location)
        if not val:
            return True
        else:
            return False
    elif typ == "ROW":
        val = sheet.row_values(location)
        if not val:
            return True
        else:
            return False
    else:
        return "You entered a type that was invalid, please enter type as either \"CELL\", \"COL\", or \"ROW\"."


def update_col(col, content):
    final_list = []
    end_point = len(content) + 1
    update_range = "{0}1:{0}{1}".format(col, end_point)
    for i in content:
        single_list = [i]
        final_list.append(single_list)
    sheet.update(update_range, final_list)


def update_row(row, content):
    end_point = len(content) + 1
    end_num, end_letter = find_row_end(end_point-1)
    set_letter = letters[end_num - 2]
    update_range = "A{1}:{2}{0}{1}".format(end_letter, row, set_letter)
    if sheet.col_count >= len(content):
        sheet.update(update_range, [content])
    else:
        add_amount = len(content) - sheet.col_count
        sheet.add_cols(add_amount)


def setup_input():
    row = 1
    col = 1
    while not is_empty((row, col), "CEL"):
        col += 1
    sheet.update_cell(row, col, "Current Row:")
    sheet.update_cell(row, col+1, 2)


def input_data(data):
    storage_col = sheet.find("Current Row:").col + 1
    cr = int(sheet.cell(1, storage_col).value)
    while not is_empty(cr, "ROW"):
        cr1 = cr + 1
        sheet.update_cell(1, storage_col, cr1)
        cr = int(sheet.cell(1, storage_col).value)
    update_row(cr, data)
    sheet.update_cell(1,storage_col,int(sheet.cell(1, storage_col).value) + 1)

# cols (int) – Number of new columns to add
setattr(sheet, "setup", setup_input)
setattr(sheet, "input_data", input_data)
setattr(sheet, "update_row", update_row)

utc_now = pytz.utc.localize(datetime.utcnow())
mst_now = utc_now.astimezone(pytz.timezone("America/Denver"))
timeV = str(mst_now.time())[0:5]
df = pytrend.trending_searches(pn='united_states')
full_list = df.head(10).values.tolist()
input = []
date = str(mst_now.date())
input.append(str(date) + " " + timeV)
for i in full_list:
    for x in i:
        input.append(x)


while True:
    try:
        sheet.find(str(date) + " " + timeV)
    except:
        sheet.input_data(input)
        print("Primary input at: {0}".format(mst_now))
    else:
        if sheet.row_values(sheet.find(str(date) + " " + timeV).row) == input:
            pass
        else:
            sheet.update_row(sheet.find(str(date) + " " + timeV).row, input)
            print("Updated input at: {0}".format(mst_now))
    td.sleep(3600)
