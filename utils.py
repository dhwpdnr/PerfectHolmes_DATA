import requests, json, os
from dotenv import load_dotenv
import pandas as pd


def get_location(address):
    load_dotenv(verbose=True)
    KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    test_data = pd.read_csv('data/test_data.csv', encoding='utf-8')
    for item in test_data.itertuples():
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + item[1]
        # for i in range(0, 5070, 1):
        #     split = []
        #     if test_data['addr'][i].endswith(']'):
        #         split = test_data['addr'][i].split('[')  # split은 리스트 반환
        #         test_data['addr'][i] = split[0]
        api_json = json.loads(str(requests.get(url, headers=headers).text))
        print(api_json['documents'][0]['address']['x'])
        print(api_json['documents'][0]['address']['y'])
        # print(f"x : {api_json['documents']['address']['x']}, y : {api_json['documents']['address']['y']}")

    return api_json
