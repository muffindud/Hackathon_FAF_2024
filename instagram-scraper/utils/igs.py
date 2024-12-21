from httpx import Client
from os import environ
from json import loads


rest_client = Client(
    headers={
        "x-ig-app-id": f"{environ.get('X-IG-APP-ID')}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)


def get_raw_data(username: str) -> dict:
    response = rest_client.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}")
    print(response)
    return loads(response.text)["data"]["user"]


def get_user_id(username: str) -> str:
    raw_data = get_raw_data(username)
    return raw_data["id"]


def get_image_url(username: str) -> dict[str, str]:
    raw_data = get_raw_data(username)
    img_url = raw_data["profile_pic_url"]
    hd_img_url = raw_data["profile_pic_url_hd"]
    return {"img_url": img_url, "hd_img_url": hd_img_url}


def get_all_posts(username: str) -> dict:
    raw_data = get_raw_data(username)
    post_count = raw_data["media_count"]
    ...


def get_posts(username: str, start_idx: int, end_idx: int) -> dict:
    # get the posts from start_idx to end_idx
    ...
