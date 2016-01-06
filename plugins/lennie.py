import requests

from will.plugin import WillPlugin
from will.decorators import hear

class LenniePlugin(WillPlugin):
    @hear("lennie")
    def get_borat(self, message):
        """
        lennie: Random!
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/lenniebot/index.php").content)
