import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class KennyPlugin(WillPlugin):
    @respond_to("what does kenny think?")
    def get_kenny(self, message):
        """
        what does kenny powers think?: Random!
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/kennybot/index.php").content)
