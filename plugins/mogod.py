import random

from will.plugin import WillPlugin
from will.decorators import respond_to, hear

class MoGodPlugin(WillPlugin):
    @hear("(mo|god){1,2}")
    @respond_to("mogod")
    def reply_to_mogod(self, message):
        """
        Mogod
        """
        self.reply(message, get_mogod_slogan())


        def get_mogod_slogan():


            godslogans = [
                "Stop praying. I'm clearly not listening.",
                "You happened because I created monkeys and got arrogant.",
                "I cannot overstate the extent to which mankind is screwed.",
                "Life is a small minority of total assholes ruining it for the vast majority of partial assholes.",
                "I give up. You're on your own. Good luck.",
                "I don't believe in evolution but at this point it would be a good idea.",
                "No matter what happens always remember: I don't care.",
                "I follow Justin Bieber because he is My son",
                "Sin-free mastrubation for all",
                "It's tough being a single Dad",
                "Update: people are still stupid",
                "Every day a billion people call My name seeking help and a billion more call it seeking orgasm. I don't know which is more awkward"
            ]

            return "(mogod) {}".format(random.choice(godslogans))
