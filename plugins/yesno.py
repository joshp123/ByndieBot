import requests
import json

from will.plugin import WillPlugin
from will.decorators import respond_to

class YesNoPlugin(WillPlugin):
    @respond_to("what do you think?")
    def get_chuck(self, message):
        """
        yesno: I will bring you an answer
        """
        self.reply(message,
                   json.loads(requests.get("http://yesno.wtf/api").content)['image'])
