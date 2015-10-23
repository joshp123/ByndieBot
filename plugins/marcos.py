from will.plugin import WillPlugin
from will.decorators import respond_to, hear


class MarcosPlugin(WillPlugin):
    @hear("( pan |^pan$)")
    @respond_to("marcos")
    def get_marcos(self, message):
        """
        marcos: Pan means bread
        """
        self.reply(message, "Pan means bread\n\n")
