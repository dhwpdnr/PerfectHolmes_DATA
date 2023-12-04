import requests, json, os
from dotenv import load_dotenv
import pandas as pd


def get_location(address):
    load_dotenv(verbose=True)
    KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    test_data = pd.read_csv('data/school_data.csv', encoding='utf-8')
    response_data = []
    for item in test_data.itertuples():
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + item[4]
        api_json = json.loads(str(requests.get(url, headers=headers).text))
        school_data = {}
        if api_json['documents'] == []:
            continue
        if "유치원" in str(item[1]):
            school_data["type"] = "유치원"
        elif "초등학교" in str(item[1]):
            school_data["type"] = "초등학교"
        elif "중학교" in str(item[1]):
            school_data["type"] = "중학교"
        elif "고등학교" in str(item[1]):
            school_data["type"] = "고등학교"

        school_data["name"] = item[1]
        school_data["address"] = item[4]
        school_data["lat"] = api_json['documents'][0]['address']['x']
        school_data["lng"] = api_json['documents'][0]['address']['y']
        response_data.append(school_data)

    return response_data
