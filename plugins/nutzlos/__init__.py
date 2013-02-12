#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: cytec@iamcytec@googlemail.com
# unnützes wissen / random german qoutes/fakts
# HTMLParser added by dschu <dschu.de>

from plugin import *
import urllib
import re
import random
from bs4 import BeautifulSoup

class nutzlos(Plugin):
	res = {
        'nutzlos': {
            'de-DE': '.*nutzlos.*'
        }
    }

	@register("de-DE", res['unnuetzes']['de-DE'])
	def nutzlos_get(self, speech, language):
		html = urllib.urlopen("http://www.unnuetzes.com/wissen/feed/").read()
		soup = BeautifulSoup(html)
		
		entries = soup.findAll("description", {"class": ""})
		
		number = random.randint(0, len(entries))
		entry = entries[number].get_text()
		
		entry = re.sub(']]>', "",entry).strip()
		
		self.say(entry)
		self.complete_request()