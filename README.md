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

### results
![Result 1](https://github.com/DonnC/zim-newspaper/blob/master/example/result_1.png)
![Result 2](https://github.com/DonnC/zim-newspaper/blob/master/example/result_2.png)
![Result 1](https://github.com/DonnC/zim-newspaper/blob/master/example/log_shot.png)
