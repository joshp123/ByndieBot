import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class SysadminPlugin(WillPlugin):
    @respond_to("sysadmin")
    def get_sysadmin(self, message):
        """
        sysadmin: I bring you sysadmin reactions
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/sysadmin/index.php").content)
