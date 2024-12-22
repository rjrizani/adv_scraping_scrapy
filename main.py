from curl_cffi import requests

def get_status_code(url):
    response = requests.get(url, impersonate="chrome")
    return response.status_code

if __name__ == "__main__":
    url = "https://id1.iherb.com/pr/california-gold-nutrition-sport-creatine-monohydrate-unflavored-1-lb-454-g/71026"
    status_code = get_status_code(url)
    print(f"Status code for {url}: {status_code}")