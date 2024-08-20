import requests
from PIL import Image
import io


URL = "https://gi-tcg-assets.guyutongxue.site/api/v2/images/"


def get_image(cid):
     url_id = URL + str(cid)
     resp = requests.get(url_id)

     print(resp)
     print(resp.headers)
     print("=" * 20)
     print(resp.content)
     webp_bytes = io.BytesIO(resp.content)
     img = Image.open(webp_bytes)
     return img