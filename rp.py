import requests
from bs4 import BeautifulSoup as bs

# n.b. I'm too fucking lazy to make a setup.py, so run pip install beautifulsoup4 and pip install requests in a venv.

def main(*args, **kwargs):
    html = requests.get('http://www.radioparadise.com/ajax_playlist_display.php?ver=1.98').text
    soup = bs(html, 'html.parser')
    now_playing = soup.find_all(id='nowplaying_title')[0].text
    print(now_playing)
    return now_playing


if __name__ == "__main__":
    # TODO: kwargs
    main()
