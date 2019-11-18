# news providers

class Providers:
    '''
        news providers. Can add additional news providers

        $ from newspaperzw.Provider import Providers
        $ Providers{"provider-name": "provider-url"})
    '''
    __NEWS_PROVIDERS__ = {
        "herald": "https://www.herald.co.zw",
        "techzim": "https://www.techzim.co.zw/",
        "sundaymail" : "http://www.sundaymail.co.zw/",
        "bulawayo24" : "https://www.bulawayo24.com/",
        "chronicle" : "http://www.chronicle.co.zw/",
        "manicapost" : "http://www.manicapost.co.zw/",
        "source" : "http://source.co.zw/",
        "dailynews" : "https://www.dailynews.co.zw/",
        "standard" : "http://www.thestandard.co.zw/",
        "nehanda" : "http://nehandaradio.com/",
        "newsnow" : "http://www.newsnow.co.uk/h/World+News/Africa/Zimbabwe",
        "financialgazette" : "http://www.financialgazette.co.zw/",
        "headlines_mole" : "https://www.sportsmole.co.uk/headlines/",
        "trend_mole" : "https://www.sportsmole.co.uk/trending",
        "footbal_mole" : "https://www.sportsmole.co.uk/football",
        "zim_supersport" : "https://www.supersport.com/football/zimbabwe",
        "soccer24" : "https://www.soccer24.co.zw/"
}

    def __init__(self, provider=None):
        self.provider = provider
        if(self.provider and type(self.provider == dict())):
            self.addProvider()

    def getProviders(self):
        return self.__NEWS_PROVIDERS__

    def addProvider(self):
        # append user provider to list
        # TODO check if provider is already available
        self.__NEWS_PROVIDERS__.update(self.provider)

    def getUrl(self, source):
        # return provider url
        if(source in self.__NEWS_PROVIDERS__):
            source = source.lower().strip()
            return self.__NEWS_PROVIDERS__[source]

        else:
            raise Exception(f"News source '{source}' not available")

    def getAll(self):
        return self.__NEWS_PROVIDERS__.values()

    def checkAdd(self, source):
        # check if adding news source have been successful
        source = source.lower().strip()
        if(self.__NEWS_PROVIDERS__[source]):
            return True
        else:
            return False