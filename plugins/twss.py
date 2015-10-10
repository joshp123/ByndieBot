from will.plugin import WillPlugin
from will.decorators import hear

twss_list = ["hard", "long", "horny", "into", "large", ]


class TWSSPlugin(WillPlugin):
    @hear(" ({}) ".format("|".join(twss_list)))
    def twss(self, message):
        """
        TWSS: I am always on the ball for things she might have said.
        """
        self.reply(message, "twss")
