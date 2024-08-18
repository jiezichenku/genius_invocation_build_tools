import requests
from PIL import Image
import io


URL = "https://gi-tcg-assets.guyutongxue.site/api/v2/images/1306"

x = requests.get(URL)

print(x)
print(x.headers)
print("=" * 20)
print(x.content)
webp_bytes = io.BytesIO(x.content)

img = Image.open(webp_bytes)
img.show()
