import time
import requests
from bs4 import BeautifulSoup as bs

from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

twss_list = ["hard", "long", "horny", "into", "large", ]

class BrandedPrepPlugin(WillPlugin):
    @respond_to("bp")
    def branded_prep(self, message):
        html = requests.get('http://redditp.com/r/pussy').text
        soup = bs(html, 'html.parser')
        now_playing = soup.find_all(id='nowplaying_title')[0].text
        img = soup.find_all('img')[0]['src'].encode('utf-8')
        self.reply(message, "Bill is playing: {}\n\n{}".format(now_playing, img))
        time.sleep(5)
        self.reply(message, "robin is gay")
        return now_playing

    @hear(" ({}) ".format("|".join(twss_list)))
    def twss(self, message):
        self.reply(message, "twss")
