import requests
import bs4

res = requests.get(
    "https://en.wikipedia.org/wiki/Brian_Chesky#:~:text=Brian%20Joseph%20Chesky%20(born%20August,76%20million%20shares%20of%20Airbnb.")

soup = bs4.BeautifulSoup(res.text, "lxml")

image_src = soup.select('.mw-file-element')

for id, image in enumerate(image_src[:2], 1):

    requests_image = requests.get('https:' + image['src'])
    file_name = f"brian_chesky_{id}.jpg"

    with open('file_name', 'wb') as file:
        file.write(requests_image.content)
