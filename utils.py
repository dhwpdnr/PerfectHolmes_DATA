import requests, json, os
from dotenv import load_dotenv


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    load_dotenv(verbose=True)
    KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    return api_json
