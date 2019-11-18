# newspaper_zim.py
# created 18 Nov 2019

from newspaperzw.news import News
from newspaperzw.Provider import Providers
from prettyprinter import pprint

# setup
# can add new provider with
# Providers(provider={'techzim': 'https://www.techzim.co.zw/'})
p = Providers()

# to get `summary` through inbuilt nlp algorithm, flag `summary=True`, requires `nltk` module
source = 'herald'
api = News(provider=source, summary=True)

try:
    print(f"[INFO] Getting news data from {p.getUrl(source)}..")

    data = api.paper()

    print("\n[INFO] News results\n")
    pprint(data)

except Exception as e:
    print("[ERROR] There was a problem: ", e)