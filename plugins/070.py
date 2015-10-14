import requests,json,HTMLParser,sys,getopt

from will.plugin import WillPlugin
from will.decorators import respond_to

class NulZeventigPlugin(WillPlugin):
    @respond_to("070")
    def nul_zeventig_plugin(self, message, argv):
		if len(argv) > 1:
			if len(sys.argv[1]) > 0:
				r = requests.get("http://looq.nl/070/index.php?text="+"{}".format("+".join(sys.argv)))
			else:
				r = requests.get("http://looq.nl/070/index.php?text=Den Haag is de mooiste stad van de wereld")
		else:
			r = requests.get("http://looq.nl/070/index.php?text=Den Haag is de mooiste stad van de wereld")
		parsed_json = json.loads(r.content)
		return(h.unescape(parsed_json['translation']))
