import requests, json, os
from dotenv import load_dotenv
import pandas as pd


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

    test_data = pd.read_csv('data/df_drop.csv', encoding='utf-8')

    for i in range(0, 5070, 1):
        split = []
        if test_data['addr'][i].endswith(']'):
            split = test_data['addr'][i].split('[')  # split은 리스트 반환
            test_data['addr'][i] = split[0]
    load_dotenv(verbose=True)
    KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    return api_json
