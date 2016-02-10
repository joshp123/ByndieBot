from random import choice

from will.plugin import WillPlugin
from will.decorators import periodic, hear


class MartijnQODPlugin(WillPlugin):

    messages = []

    @hear('\\W+')
    def store_message(self, message):
        sentence = str(message)
        words = sentence.split(' ')
        max_word_len = max([len(w) for w in words])
        if message.sender.name == 'Martijn Meijer' and\
                len(sentence) > 20 and\
                max_word_len > 5:
            self.messages.append(sentence)

    @periodic(hour='16', minute='0', day_of_week='mon-fri')
    def say_quote(self):
        q = choice(self.messages)
        self.say('Martijn Quote of the Day!')
        self.say('/quote {}'.format(q))
        self.messages = []  # empty list to prepare for next day
