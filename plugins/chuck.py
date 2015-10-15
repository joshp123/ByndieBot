import requests

from will.plugin import WillPlugin
from will.decorators import respond_to


class ChuckPlugin(WillPlugin):
    @respond_to("chuck")
    def get_chuck(self, message):
        """
        chuck: I bring you wisdom.
        """
        random_joke = requests.get("http://api.icndb.com/jokes/random").json()
        self.reply(message, random_joke['value']['joke'])
