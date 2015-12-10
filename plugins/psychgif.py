import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class PsychPlugin(WillPlugin):
    @respond_to("psychgif")
    def get_psycht(self, message):
        """
        psychgif: I psych you out...
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/psychgif/index.php").content)
