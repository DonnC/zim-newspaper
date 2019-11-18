# newspaper_zim.py
# created 18 Nov 2019

from newspaperzw.news import News
from prettyprinter import pprint

api = News()

try:
    print("[INFO] Getting news data..")

    data = api.paper()
    pprint(data)

except Exception as e:
    print("[ERROR] There was a problem: ", e)