import requests
import json

from will.plugin import WillPlugin
from will.decorators import respond_to


class ChuckPlugin(WillPlugin):
    @respond_to("chuck")
    def get_chuck(self, message):
        """
        chuck: I bring you wisdom.
        """
        self.reply(message,
                   json.loads(requests.get("http://api.icndb.com/jokes/random").content)['value']['joke'])
