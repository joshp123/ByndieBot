import datetime
import pytz
from random import randint

from will.plugin import WillPlugin
from will.decorators import respond_to

class BostonBeerTimePlugin(WillPlugin):
    @respond_to("bostonbeer")
    def reply_to_bostonbeertime(self, message):
        """
        bostonbeer: I tell you how long it is until Boston has their beers.
        """
        self.reply(message, get_bostonbeer_slogan())


def get_bostonbeer_slogan():
    now = datetime.datetime.now()
    now = = now.replace(hour=-6)
    today = datetime.date.today()
    today = today.replace(hour=-6)
    todaybeeroclock = now.replace(hour=17, minute=00, second=00)
    todayendbeeroclock = now.replace(hour=18, minute=00, second=00)
    todayend = now.replace(hour=23, minute=59, second=59)
    todaystartworkday = now.replace(hour=9, minute=0, second=0)
    tomorrowbeeroclock = now.replace(hour=17, minute=00, second=00) + datetime.timedelta(days=1)
    nextmondaybeeroclock = now.replace(hour=17, minute=00, second=00) + datetime.timedelta(weeks=1)
    weekday = today.weekday()

    formatcountdown = todaybeeroclock - now


    if now < todayend and weekday >= 0 and weekday <= 4:
        start = (now-todaystartworkday).total_seconds()

        if now < todayendbeeroclock and now >= todaybeeroclock:
            countdown = ((todayendbeeroclock - now).total_seconds())+start
            formatcountdown = todayendbeeroclock - now
        elif now < todayendbeeroclock and now >= todaybeeroclock:
            countdown = ((tomorrowbeeroclock - now).total_seconds())+start
            formatcountdown = tomorrowbeeroclock - now
        else:
            countdown = ((todaybeeroclock - now).total_seconds())+start
            formatcountdown = todaybeeroclock - now
    else:
        start = (now-nextmondaybeeroclock).total_seconds()
        countdown = ((nextmondaybeeroclock - now).total_seconds())+start

    beertimeslogans = [
        "It's BEER time! Go on, you know you want one...",
        "I got 99 problems & BEERTIME solves all of 'em",
        "Trust me, you can dance...BEERTIME!",
        "Take one, it won’t slow you down!",
        "A hard earned thirst needs a big cold beer",
        "Have a BEER, It's the most natural thing in the world",
        "Remember! Beer as food-value, but food does not have beer-value",
        "BEER will save the world! I don't know how, but it will",
        "BEER! I only drink to make YOU more interesting",
        "Hey, looks like its BEERTIME, better grab me a cold one",
        "Drink good BEER, with GOOD friends",
        "The party is not over till the beer is in the belly",
        "All your BEER are belong to us",
        "I need to do something about my Guzzelitis",
        "My idea of a balanced diet is a BEER in each hand",
        "Jesse will come soon, he WILL be the HERO of your day",
        "A beer a day keeps the doctor away. Have one!",
        "Shhh...Yep, I hear a BEER calling me",
        "Friends bring happiness into your life, best friends bring BEER!",
        "It makes you see double...and feel single. Have one!"
    ]

    tooearlyslogans = [
        "It's too early for BEER, you could have a problem...",
        "Be smart...Be safe...Be sober...",
        "Addiction is self-destruction...",
        "And they all claim they can stop drinking any time they want to...",
        "Come on man...",
        "Less drinking, more thinking...",
        "Alcohol is a parent to domestic violence...",
        "Drink water...refresh, rehydrate, replenish..."
    ]

    weekendlogans = ["FFS... it's the WEEKEND, go home and relax!"]

    s = formatcountdown.seconds
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)

    if weekday > 4:
        return "(borat) {}".format(weekendlogans[randint(0, len(weekendlogans) - 1)])
    elif now < todayendbeeroclock and now >= todaybeeroclock:
        return "(borat) {}".format(beertimeslogans[randint(0, len(beertimeslogans) - 1)])
    else:
        return "(borat) {}just wait another {} hours {} minutes and {} seconds".format(
            tooearlyslogans[randint(0, len(tooearlyslogans) - 1)], h, m, s)
