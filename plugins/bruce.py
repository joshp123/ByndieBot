import requests

from will.plugin import WillPlugin
from will.decorators import hear

class BrucePlugin(WillPlugin):
    @hear("bruce")
    def get_bruce(self, message):
        """
        bruce: Bruce Schneier
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/bruce/index.php").content)
