# zim-newspaper
library to get newspaper, news from zim leading news providers

### Example
``` py
from newspaperzw.Provider import Providers
from newspaperzw.news import News

# add your favourite news source so as to use its name only when getting news data
p = Providers(provider={'techzim': 'https://www.techzim.co.zw/'})

# get all preset news sources and url
all = Providers().getAll()

try:
  # get data from news site by name, default = `herald`
  api       = News(provider='techzim')
  news_data =  api.paper()
  
  # return dict with all news data, best to use `prettyprinter`
  print(new_data)
  
except Exception as e:
  print("There was a problem: ", e)
```

## Get summary of article
- to get summary through NLP function, ```nltk``` is needed as dependent
- this returns same results as above but with a summary attribute that contains a summary of the article

```py
from newspaperzw.Provider import Providers
from newspaperzw.news import News

try:
  # get data from news site by name, default = `herald`
  api       = News(provider='techzim', summary=True)
  news_data =  api.paper()
  
  # return dict with all news data, best to use `prettyprinter`
  print(new_data)
  
except Exception as e:
  print("There was a problem: ", e)
```

### NEW! 
#### added flag to set or disable cache 
```py
# __version__1.1.0

from newspaperzw.Provider import Providers
from newspaperzw.news import News

'''
	get a summary of the article from each article through the `summary=True` flag
	avoid cache memory by disabling it through the `cache=False` flag
	if cache is True, it will not return news previously downloaded on previous runs
'''

try:
  # get data from news site by name, default = `herald`
  api       = News(provider='techzim', summary=True, cache=False)
  news_data =  api.paper()
  
  # return dict with all news data, best to use `prettyprinter`
  print(new_data)
  
except Exception as e:
  print("There was a problem: ", e)
```

## TODO
- library scrapes all available data that it encounters, need to narrow it down by date/month/year
- start from `today` up to any news obtained from `last year`
- improve speed
- disble logging
- date published

- log files need to be deleted in case they occupy signficant space on disk