from will.plugin import WillPlugin
from will.decorators import respond_to


class ChuckPlugin(WillPlugin):
    @respond_to("marcos")
    def get_chuck(self, message):
        """
        marcos: Pan means bread
        """
        self.reply(message,"Pan means bread")
