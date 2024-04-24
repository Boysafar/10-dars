import requests
import bs4

res = requests.get(
    "https://en.wikipedia.org/wiki/Brian_Chesky#:~:text=Brian%20Joseph%20Chesky%20(born%20August,76%20million%20shares%20of%20Airbnb.")

soup = bs4.BeautifulSoup(res.text, "lxml")

image_src = soup.select('.mw-file-element')

for image in image_src:
    requests_image = requests.get('https:' + image['src'])

    with open('brian_chesky.jpg', 'wb') as file:
        file.write(requests_image.content)
