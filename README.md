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

## TODO
- sometimes news articles are not downloaded after multiple runs on a news source, because of caching
- set flag that enables or disables `cache`
- library scrapes all available data that it encounters, need to narrow it down by date/month/year
- start from `today` up to any news obtained from `last year`
- improve speed
- exception handling

### results
![Result 1](https://github.com/DonnC/zim-newspaper/blob/master/example/result_1.png)
![Result 2](https://github.com/DonnC/zim-newspaper/blob/master/example/result_2.png)
![Result 1](https://github.com/DonnC/zim-newspaper/blob/master/example/log_shot.png)
