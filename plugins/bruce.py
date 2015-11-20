import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class CryptoPlugin(WillPlugin):
    @respond_to("crypto")
    def get_crypto(self, message):
        """
        crypto: Bruce Schneier facts
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/bruce/index.php").content)
