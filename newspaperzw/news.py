import newspaper
from newspaperzw.Provider import Providers
from random import randint
import logging
import datetime

class News:
    '''
        get news from zim online news provider

    '''
    __title__ = 'newspaperzw'
    __author__ = 'Donald Chinhuru'
    __license__ = 'MIT'
    __copyright__ = 'Copyright 2019, Donald Chinhuru'

    def __init__(self, provider='herald', summary=False):
        self.provider   = provider
        self.summary    = summary
        self.nlp        = False
        self.error_msg  = ""
        self.now_time   = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        logging.basicConfig(level=logging.DEBUG, filename=f'./news_{self.now_time}.log', format = '%(asctime)s - %(levelname)s - %(message)s')

        self.checkNlp()

    def checkNlp(self):
        if(self.summary):
            # needs nltk library
            try:
                import nltk
                self.nlp= True

            except ImportError as e:
                self.error_msg = f"{e}\n`nltk` module is needed for NLP functionality!. Try\n$ pip install nltk.\n$ nltk.download()"

    def paper(self):
        '''
            get newspaper articles, default source is `herald` newspaper
            defaults to articles of this month and year
            import newspaperzw

            news = newspaperzw.news()
        '''

        if self.summary and self.nlp == False:
            # raise exception. `nltk` module missing
            raise Exception(self.error_msg)

        news_source = Providers().getUrl(self.provider).strip()

        name = newspaper.Source(news_source)
        name.build()
        name.download()
        name.parse()
        name.download_articles()

        # do logging
        logging.debug(f"News Source build and downloaded. url: {news_source}")

        news_data = {}
        news_article = []

        counter = 0
        for article in name.article_urls():
            images = ""
            keywords = ""

            try:
                name.articles[counter].download()
                name.articles[counter].parse()

                # log
                logging.debug(f"Article #{counter} downloaded and parsed successfuly")

            except:
                counter += 1

                # log
                logging.error(f"Error download and parsing article #{counter}. continue..")
                continue

            # get in data
            title       = name.articles[counter].title
            date_pub    = name.articles[counter].publish_date
            top_image   = name.articles[counter].top_image
            link        = name.articles[counter].url
            text        = name.articles[counter].text

            if(self.nlp):
                # do nlp stuff
                name.articles[counter].nlp()
                summary     = name.articles[counter].summary

                for words in name.articles[counter].keywords:
                    keywords += str(words) + ','

                # log
                logging.debug(f"summary flag enabled. NLP summary obtained successfuly")

            # add to news pool, only add news of this year and month
            # data_pub format = 10-04-2018 21:28:09
            data = {}
            if(self.nlp):
                data.update({
                    "article_id": randint(555, 999),
                    "title": title,
                    "published": date_pub,
                    "image": top_image,
                    "news": text,
                    "summary": summary,
                    "keywords": keywords.rstip(','),
                    "url": link
                })

                # log
                logging.debug("article data with summary saved to news pool!")

            else:
                data.update({
                    "article_id": randint(555, 999),
                    "title": title,
                    "published": date_pub,
                    "image": top_image,
                    "news": text,
                    "url": link
                })

                # log
                logging.debug("article data added to news pool")

            news_article.append(data)
            data = {}

            # increment to next articles
            counter += 1

        # build main news storage
        news_data.update({
            'source': name.brand,
            'domain': name.domain,
            'news': news_article
        })

        # log
        logging.debug("News main data pool created on success")

        return news_data