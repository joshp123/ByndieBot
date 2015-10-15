import requests,json,HTMLParser

from will.plugin import WillPlugin
from will.decorators import respond_to

class NulZeventigPlugin(WillPlugin):
	@respond_to("070 (?<text>.*)")
	def nul_zeventig_plugin(self, message, text='Den Haag is de mooiste stad van de wereld'):
		h = HTMLParser.HTMLParser()
		r = requests.get("http://looq.nl/070/index.php?text="+"{}".format("+".join(text)))
		parsed_json = json.loads(r.content)
		return(h.unescape(parsed_json['translation']))
