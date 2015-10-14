from will.plugin import WillPlugin

twss_list = ("hard", "long", "horny", "into", "large",)


class TWSSPlugin(WillPlugin):
    def twss(self, message):
        """
        TWSS: I am always on the ball for things she might have said.
        """
        self.reply(message, "twss")
