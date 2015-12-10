
import requests
import json

from will.plugin import WillPlugin
from will.decorators import respond_to

class ChuckPlugin(WillPlugin):
    @respond_to("psychgif")
    def get_skeet(self, message):
        """
        psychgif: I psych you out...
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/psychgif/index.php").content)
