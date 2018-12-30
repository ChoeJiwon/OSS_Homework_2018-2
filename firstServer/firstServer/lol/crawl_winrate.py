import codecs
import re
import requests
import lxml
from bs4 import BeautifulSoup


def get_Winrate(mChamp,eChamp,pos):
    url = 'http://www.op.gg/champion/' + mChamp + '/statistics/' + pos + '/counter/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    #output = soup.find('div',{'class' : 'champion-matchup-champion-list'});
    output = soup.find('div',{'data-champion-key' : eChamp});
    output = output.find('span', {'class':'champion-matchup-list__winrate'});


    output = output.text
    output = output.split('\t\t\t\t\t\t\t');
    output = output[1].split('\t');
    output = output[1].split('\n');

    i=output[0].split('%');
    i=float(i[0]);

    return i;
