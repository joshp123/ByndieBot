import requests,json,HTMLParser,sys,getopt

from will.plugin import WillPlugin
from will.decorators import respond_to

class NulDertigPlugin(WillPlugin):
    @respond_to("030")
    def nul_dertig_plugin(self, message, argv):
		if len(argv) > 1:
			if len(sys.argv[1]) > 0:
				r = requests.get("http://looq.nl/030/index.php?text="+"{}".format("+".join(sys.argv)))
			else:
				r = requests.get("http://looq.nl/030/index.php?text=Den Haag is de mooiste stad van de wereld")
		else:
			r = requests.get("http://looq.nl/030/index.php?text=Den Haag is de mooiste stad van de wereld")
		parsed_json = json.loads(r.content)
		return(h.unescape(parsed_json['translation']))
