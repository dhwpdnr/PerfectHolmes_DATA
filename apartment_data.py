import pandas as pd

# data/current_apartment.csv 읽고 데이터 확인하기
current_apartment = pd.read_csv('data/current_apartment.csv', encoding='cp949')
actual_transaction = pd.read_csv('data/actual_transaction.csv', encoding='cp949')
# print(current_apartment.head())
# print(actual_transaction.head())

current_apartment_col = current_apartment.columns
actual_transaction_col = actual_transaction.columns

apartment_list = []
for item in current_apartment.itertuples():
    apartment_data = {}
    apartment_data["행정동"] = item.행정동
    apartment_data["단지명"] = item.단지명
    apartment_data["지번주소"] = item.지번주소
    apartment_data["도로명주소"] = item.도로명주소
    apartment_data["세대수"] = item.세대수

    # apartment_data[item[5]] = item[6]

    apartment_list.append(apartment_data)

from pprint import pprint

# pprint(apartment_list)

actual_transaction_col_list = actual_transaction.iloc[5]

# for item in actual_transaction_col_list:
#     print(item)
#
# print(actual_transaction_col_list[1])

for item in actual_transaction.iloc[6:].itertuples():
    for i in range(len(item)):
        print(actual_transaction_col_list[i], item[i+1])

# apartment_list 를 data 폴더에 저장하기
import json

with open('data/apartment_data.json', 'w', encoding='utf-8') as f:
    json.dump(apartment_list, f, ensure_ascii=False, indent=4)
