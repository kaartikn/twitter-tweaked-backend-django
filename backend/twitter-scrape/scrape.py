import snscrape.modules.twitter as sntwitter

def advancedSearch(searchQuery, limit = 1):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(searchQuery).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.user.username, tweet.content, tweet.date])
    print(tweets)

advancedSearch("liverpool")

def queryBuilder(allWordsQuery : str = "", exactPhrase: str = "", anyOfTheseWords: list = [], noneOfTheseWords: list = [], theseHashtags: list = [], language: str = "", fromAccounts: list = [], toAccounts: list = [], mentioningAccounts: list = [], showReplies: bool = True, onlyShowReplies: bool = False, showLinks: bool = False, onlyShowTweetsWithLink: bool = False, minimumReplies: int = 0, minimumFaves: int = 0, minimumRTs: int = 0, fromDate: str = "", toDate: str = ""):
    exactPhraseQuery = exactPhraseQueryBuilder(exactPhrase)
    anyWordsQuery = anyOfWordQueryBuilder(anyOfTheseWords)
    noneWordsQuery = noneOfWordQueryBuilder(noneOfTheseWords)
    anyHashtagQuery = anyOfHashtagQueryBuilder(theseHashtags)
    fromAccountsQuery = fromAccountsQueryBuilder(fromAccounts)
    toAccountsQuery = toAccountsQueryBuilder(toAccounts)
    mentioningAccountsQuery = mentioningAccountsQueryBuilder(mentioningAccounts)
    minRepliesQuery = minimumRepliesQueryBuilder(minimumReplies)
    minFavesQuery = minimumFavesQueryBuilder(minimumFaves)
    minRTsQuery = minimumRTsQueryBuilder(minimumRTs)
    languageQuery = languageFilterQueryBuilder(language)
    toDateQuery = toDateQueryBuilder(toDate)
    fromDateQuery = fromDateQueryBuilder(fromDate)
    repliesFilterQuery = repliesFilterQueryBuilder(showReplies, onlyShowReplies)
    linksFilterQuery =  linksFilterQueryBuilder(showLinks, onlyShowTweetsWithLink)

    query = queryBuilder(allWordsQuery, exactPhraseQuery, anyWordsQuery, noneWordsQuery, anyHashtagQuery, fromAccountsQuery, toAccountsQuery, mentioningAccountsQuery, minRepliesQuery, minFavesQuery, minRTsQuery, languageQuery, toDateQuery, fromDateQuery, repliesFilterQuery, linksFilterQuery)
    return query

def exactPhraseQueryBuilder(exactPhrase: str):
    return "" if exactPhrase == "" else '"{exactPhrase}"'.format(exactPhrase=exactPhrase)

def anyOfWordQueryBuilder(wordList: list):
    any_query = ""
    if wordList != []:
        any_query = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx < list_length):
                any_query += "{word} OR ".format(word=word)
            else:
                any_query += "{word})".format(word=word)
    return any_query

def noneOfWordQueryBuilder(wordList: list):
    none_query = ""
    if (wordList != []):
        for word in wordList:
            none_query += "-{word} ".format(word=word)
    return none_query

def anyOfHashtagQueryBuilder(wordList: list):
    any_hashtag = ""
    if (wordList != []):
        any_hashtag = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx < list_length):
                any_hashtag += "#{word} OR ".format(word=word)
            else:
                any_hashtag += "#{word})".format(word=word)
    return any_hashtag

def fromAccountsQueryBuilder(wordList: list):
    from_accounts = ""
    if(wordList != []):
        from_accounts = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx < list_length):
                from_accounts += "from:{word} OR ".format(word=word)
            else:
                from_accounts += "{word})".format(word=word)
    return from_accounts

def toAccountsQueryBuilder(wordList: list):
    to_accounts = ""
    if(wordList != []):
        to_accounts = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx < list_length):
                to_accounts += "to:{word} OR ".format(word=word)
            else:
                to_accounts += "{word})".format(word=word)
    return to_accounts


def mentioningAccountsQueryBuilder(wordList: list):
    mentioning_accounts = ""
    if(wordList != []):
        mentioning_accounts = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx < list_length):
                mentioning_accounts += "@{word} OR ".format(word=word)
            else:
                mentioning_accounts += "@{word})".format(word=word)
    return mentioning_accounts

def minimumRepliesQueryBuilder(filterNumber: int):
    return "" if filterNumber == 0 else "min_replies:{minReplies}".format(minReplies = filterNumber)

def minimumFavesQueryBuilder(filterNumber: int):
    return "" if filterNumber == 0 else "min_faves:{minFaves}".format(minFaves = filterNumber)

def minimumRTsQueryBuilder(filterNumber: int):
    return "" if filterNumber == 0 else "min_retweets:{minRTs}".format(minRTs = filterNumber)

def languageFilterQueryBuilder(language: str):
    return "" if language == "" else "lang:{language}".format(language = language)

def toDateQueryBuilder(toDate: str):
    return "" if toDate == "" else "until:{toDate}".format(toDate=toDate)

def fromDateQueryBuilder(fromDate: str):
    return "" if fromDate == "" else "since:{fromDate}".format(fromDate=fromDate)

def repliesFilterQueryBuilder(showReplies: bool, onlyShowReplies: bool):
    return "-filter:replies" if showReplies == False else ("filter:replies" if showReplies==True and onlyShowReplies==True else "")

def linksFilterQueryBuilder(showLinks: bool, onlyShowTweetsWithLink: bool):
    return "-filter:links" if showLinks == False else ("filter:links" if showLinks==True and onlyShowTweetsWithLink==True else "")

def queryBuilder(allWordsQuery: str, exactPhraseQuery: str, anyWordsQuery: str, noneWordsQuery: str, anyHashTagQuery: str, fromAccountsQuery: str, toAccountsQuery: str, mentioningAccountsQuery: str, minRepliesQuery: str, minFavesQuery: str, minRTsQuery: str, languagesQuery:str, toDateQuery: str, fromDateQuery: str, repliesFilterQuery: str, linksFilterQuery: str):
    query = "{allWordsQuery} {exactPhraseQuery} {anyWordsQuery} {noneWordsQuery} {anyHashTagQuery} {fromAccountsQuery} {toAccountsQuery} {mentioningAccountsQuery} {minRepliesQuery} {minFavesQuery} {minRTsQuery} {languageQuery} {toDateQuery} {fromDateQuery} {repliesFilterQuery} {linksFilterQuery}".format(allWordsQuery=allWordsQuery, exactPhraseQuery = exactPhraseQuery, anyWordsQuery=anyWordsQuery, noneWordsQuery=noneWordsQuery, anyHashtagQuery=anyHashTagQuery, fromAccountsQuery=fromAccountsQuery, toAccountsQuery=toAccountsQuery, mentioningAccountsQuery=mentioningAccountsQuery, minRepliesQuery=minRepliesQuery, minFavesQuery=minFavesQuery, minRTsQuery=minRTsQuery, languageQuery=languagesQuery, toDateQuery=toDateQuery, fromDateQuery=fromDateQuery, repliesFilterQuery=repliesFilterQuery, linksFilterQuery=linksFilterQuery)
    return query.strip()