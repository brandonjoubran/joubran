from bs4 import BeautifulSoup
import requests
import os
import PIL
from PIL import Image

#address = "https://instagram.fyyz1-2.fna.fbcdn.net/vp/707db158bb6cff640718b5666f1b5c68/5E3DD9D7/t51.2885-19/s150x150/69100588_1146658652184861_4560228083973488640_n.jpg?_nc_ht=instagram.fyyz1-2.fna.fbcdn.net"

'''page = requests.get(address)
parse = BeautifulSoup(page.text, 'html.parser')

memes = parse.findAll('img')

if(not os.path.exists('Memes')):
    os.makedirs('Memes')

os.chdir('Memes')

file_list = os.listdir('.')
acc = len(file_list)

for meme in memes:
    try:
        url = meme['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('meme-' + str(acc) + '.jpg', 'wb') as file:
                file.write(requests.get(url).content)
                file.close()
                acc += 1
    except:
        print("failed")
        pass'''


class Pic_Scraper:

    def scrape(self, address, dir):

        page = requests.get(address)
        parse = BeautifulSoup(page.text, 'html.parser')

        memes = parse.findAll('img')

        if (not os.path.exists(dir)):
            os.makedirs('Scraped')

        os.chdir(dir)

        file_list = os.listdir('.')
        acc = len(file_list)

        for meme in memes:
            try:
                url = meme['src']
                source = requests.get(url)
                if source.status_code == 200:
                    with open('meme-' + str(acc) + '.jpg', 'wb') as file:
                        file.write(requests.get(url).content)
                        file.close()
                        acc += 1
            except:
                print("failed")
                pass

    def resize(self, path="Scraped"):
        os.chdir(path)

        file_list = os.listdir('.')
        size = len(file_list)

        for num in range(size - 1):
            try:
                img = Image.open('meme-' + str(num) + '-resized.jpg')
                img = img.resize((1080, 1080), PIL.Image.ANTIALIAS)
                img.save('meme-' + str(num) + '-resized.jpg')
            except:
                pass

