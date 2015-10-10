from will.plugin import WillPlugin
from will.decorators import hear

twss_list = ["hard", "long", "horny", "into", "large", ]


class TWSSPlugin(WillPlugin):
    @hear(" ({}) ".format("|".join(twss_list)))
    def twss(self, message):
        self.reply(message, "twss")
