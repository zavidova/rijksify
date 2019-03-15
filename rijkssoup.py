import urllib2
from bs4 import BeautifulSoup
import sys
import requests
import pprint
import re
import pyperclip


reload(sys)
sys.setdefaultencoding('utf8')


#all the individual artists' profile pages go there

urls = ['https://www.rijksakademie.nl/NL/resident/immaculate-anderu-mali',
'https://www.rijksakademie.nl/NL/resident/ozgur-atlagan',
'https://www.rijksakademie.nl/NL/resident/sujin-bae-jonathan-lemke',
'https://www.rijksakademie.nl/NL/resident/salim-bayri',
'https://www.rijksakademie.nl/NL/resident/kevin-bray',
'https://www.rijksakademie.nl/NL/resident/omar-a-chowdhury',
'https://www.rijksakademie.nl/NL/resident/morgan-courtois',
'https://www.rijksakademie.nl/NL/resident/jude-crilly',
'https://www.rijksakademie.nl/NL/resident/sara-culmann',
'https://www.rijksakademie.nl/NL/resident/tanja-engelberts',
'https://www.rijksakademie.nl/NL/resident/aldo-esparza-ramos',
'https://www.rijksakademie.nl/NL/resident/aslan-gaisumov',
'https://www.rijksakademie.nl/NL/resident/lotte-van-geijn',
'https://www.rijksakademie.nl/NL/resident/catalina-gonzalez',
'https://www.rijksakademie.nl/NL/resident/lungiswa-gqunta',
'https://www.rijksakademie.nl/NL/resident/elleke-hageman',
'https://www.rijksakademie.nl/NL/resident/omar-imam',
'https://www.rijksakademie.nl/NL/resident/artor-jesus-inkero',
'https://www.rijksakademie.nl/NL/resident/florence-jung',
'https://www.rijksakademie.nl/NL/resident/donghwan-kam',
'https://www.rijksakademie.nl/NL/resident/arturo-kameya',
'https://www.rijksakademie.nl/NL/resident/ozgur-kar',
'https://www.rijksakademie.nl/NL/resident/maria-kley',
'https://www.rijksakademie.nl/NL/resident/mire-lee',
'https://www.rijksakademie.nl/NL/resident/sheng-wen-lo',
'https://www.rijksakademie.nl/NL/resident/georgia-lucas-going',
'https://www.rijksakademie.nl/NL/resident/christopher-mahon',
'https://www.rijksakademie.nl/NL/resident/silvia-martes',
'https://www.rijksakademie.nl/NL/resident/astrid-nobel',
'https://www.rijksakademie.nl/NL/resident/ima-abasi-okon',
'https://www.rijksakademie.nl/NL/resident/ian-page',
'https://www.rijksakademie.nl/NL/resident/molly-palmer',
'https://www.rijksakademie.nl/NL/resident/yashaswini-raghunandan',
'https://www.rijksakademie.nl/NL/resident/eoghan-ryan',
'https://www.rijksakademie.nl/NL/resident/bert-scholten',
'https://www.rijksakademie.nl/NL/resident/mette-sterre',
'https://www.rijksakademie.nl/NL/resident/zamir-suleymanov',
'https://www.rijksakademie.nl/NL/resident/kanitha-tith',
'https://www.rijksakademie.nl/NL/resident/remco-torenbosch',
'https://www.rijksakademie.nl/NL/resident/omar-vega-macotela',
'https://www.rijksakademie.nl/NL/resident/arian-de-vette',
'https://www.rijksakademie.nl/NL/resident/marit-westerhuis',
'https://www.rijksakademie.nl/NL/resident/marina-xenofontos',
'https://www.rijksakademie.nl/NL/resident/shen-xin',
'https://www.rijksakademie.nl/NL/resident/dan-zhu'
]


for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content_box = soup.find('div', attrs={'class': 'resident_content'})
    content = content_box.text.strip()
    print (content)
