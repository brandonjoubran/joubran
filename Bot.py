
from InstagramAPI import InstagramAPI
import os
import time
import requests

class Bot:

    def __init__(self, username, password):
        self.account = InstagramAPI(username, password)
        self.account.login()
        #account.getUsernameInfo(username)
        req = requests.get('https://api.instagram.com/oembed/?url={}'.format('https://www.instagram.com/p/B2riIVNhwar/'))

    def comment(self, message, post_url, amount):
        req = requests.get('https://api.instagram.com/oembed/?url={}'.format(post_url))
        media_id = req.json()['media_id']
        for i in range(amount):
            try:
                print("Trying...")
                self.account.comment(media_id, message)
                time.sleep(120)
            except:
                print("Failed...")
                pass

    def delete_post(self, post_url):
        media_id = self.req.json()['media_id']
        self.account.deleteMedia(media_id)

    def upload_post(self, path, caption):
        os.chdir(path)
        for pic in os.listdir('.'):
            self.account.uploadPhoto(pic, caption=caption)
            time.sleep(10)

    def follow(self, username):
        url = 'https://www.instagram.com/' + username + '/?__a=1'
        req = requests.get(url)
        follow_list = ['1399376725', '236279329']

        #print(req.json()['logging_page_id'])
        id = req.json()
        print(id['graphql']['user']['id'])
        self.account.follow(id['graphql']['user']['id'])