import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class KennyPlugin(WillPlugin):
    @hear("kenny?")
    def get_kenny(self, message):
        """
        kenny?: gives an honest reply from kenny powers not always sfw
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/kennybot/index.php").content)
