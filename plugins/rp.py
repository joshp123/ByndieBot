import requests
from bs4 import BeautifulSoup as bs

from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

class RadioParadisePlugin(WillPlugin):
    @respond_to("rp")
    def radio_paradise(self, message):
        html = requests.get('http://www.radioparadise.com/ajax_playlist_display.php?ver=1.98').text
        soup = bs(html, 'html.parser')
        now_playing = soup.find_all(id='nowplaying_title')[0].text
        img = soup.find_all('img')[0]['src'].encode('utf-8')
        self.reply(message, "(bill) is playing: {}\n\n{}".format(now_playing, img))
        return now_playing

