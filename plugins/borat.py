import requests

from will.plugin import WillPlugin
from will.decorators import hear

class BoratPlugin(WillPlugin):
    @hear("borat")
    def get_borat(self, message):
        """
        borat: Jagshemash!
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/borat/index.php").content)
