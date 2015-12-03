import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

class WhatTheCommitPlugin(WillPlugin):
    @respond_to("commit")
    def get_commit(self, message):
        """
        commit: Random commit message
        """
        self.reply(message,
                   requests.get("http://www.looq.nl/commit/index.php").content)
