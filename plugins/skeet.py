import requests

from will.plugin import WillPlugin
from will.decorators import hear

class SkeetPlugin(WillPlugin):
    @hear("skeet")
    def get_skeet(self, message):
        """
        skeet: The main man on stackoverflow
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/skeet/index.php").content)
