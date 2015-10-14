from will.plugin import WillPlugin
from will.decorators import respond_to


class MarcosPlugin(WillPlugin):
    @respond_to("marcos")
    def get_marcos(self, message):
        """
        marcos: Pan means bread
        """
        self.reply(message,"Pan means bread")
