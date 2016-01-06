import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class LenniePlugin(WillPlugin):
    @respond_to("what does lennie think?")
    def get_borat(self, message):
        """
        what does lennie think?: Random!
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/lenniebot/index.php").content)
