import requests

from will.plugin import WillPlugin
from will.decorators import respond_to


class CatGifPlugin(WillPlugin):
    @respond_to("catgif")
    def get_cat_gif(self, message):
        """
        catgif: I bring you gifs of cats.
        """
        self.reply(message,
                   requests.get("http://looq.nl/cat/index.php").content)
