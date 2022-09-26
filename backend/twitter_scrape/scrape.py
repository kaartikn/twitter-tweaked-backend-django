import snscrape.modules.twitter as sntwitter
import jsons

from backend.misc.misc import formatResponseTweetJSON

def advancedSearch(searchQuery, limit = 10):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(searchQuery).get_items():
        if len(tweets) == limit:
            break
        else:
            formattedTweet = formatResponseTweetJSON(tweet.url, tweet.date, tweet.content, tweet.renderedContent, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, (tweet.media) if (tweet.media is None) else (jsons.dumps(tweet.media)), tweet.quotedTweet, tweet.user.username, tweet.user.displayname, tweet.user.verified, tweet.user.profileImageUrl, tweet.user.linkUrl)
            tweets.append(formattedTweet)
    return tweets

def queryBuilder(allWordsQuery : str = "", exactPhrase: str = "", anyOfTheseWords: list = [], noneOfTheseWords: list = [], theseHashtags: list = [], fromAccounts: list = [], toAccounts: list = [], mentioningAccounts: list = [], minimumReplies: int = 0, minimumFaves: int = 0, minimumRTs: int = 0, language: str = "", toDate: str = "", fromDate: str = "",  showReplies: bool = True, onlyShowReplies: bool = False, showLinks: bool = False, onlyShowTweetsWithLink: bool = False):
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

    query = queryBuilderFinal(allWordsQuery=allWordsQuery, exactPhraseQuery=exactPhraseQuery, anyWordsQuery=anyWordsQuery, noneWordsQuery=noneWordsQuery, hashtagQuery=anyHashtagQuery, fromAccountsQuery=fromAccountsQuery, toAccountsQuery=toAccountsQuery, mentioningAccountsQuery=mentioningAccountsQuery, minRepliesQuery=minRepliesQuery, minFavesQuery=minFavesQuery, minRTsQuery=minRTsQuery, languagesQuery=languageQuery, toDateQuery=toDateQuery, fromDateQuery=fromDateQuery, repliesFilterQuery=repliesFilterQuery, linksFilterQuery=linksFilterQuery)
    return query

def exactPhraseQueryBuilder(exactPhrase: str):
    return "" if exactPhrase == "" else '"{exactPhrase}"'.format(exactPhrase=exactPhrase)

def anyOfWordQueryBuilder(wordList: list):
    any_query = ""
    if wordList != []:
        any_query = "("
        list_length = len(wordList)
        for idx, word in enumerate(wordList):
            if(idx + 1 < list_length):
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
            if(idx + 1 < list_length):
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
            if(idx + 1 < list_length):
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
            if(idx + 1 < list_length):
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
            if(idx + 1 < list_length):
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

def queryBuilderFinal(allWordsQuery: str, exactPhraseQuery: str, anyWordsQuery: str, noneWordsQuery: str, hashtagQuery: str, fromAccountsQuery: str, toAccountsQuery: str, mentioningAccountsQuery: str, minRepliesQuery: str, minFavesQuery: str, minRTsQuery: str, languagesQuery:str, toDateQuery: str, fromDateQuery: str, repliesFilterQuery: str, linksFilterQuery: str):
    query = "{allWordsQuery} {exactPhraseQuery} {anyWordsQuery} {noneWordsQuery} {anyHashTagQuery} {fromAccountsQuery} {toAccountsQuery} {mentioningAccountsQuery} {minRepliesQuery} {minFavesQuery} {minRTsQuery} {languageQuery} {toDateQuery} {fromDateQuery} {repliesFilterQuery} {linksFilterQuery}".format(allWordsQuery=allWordsQuery, exactPhraseQuery = exactPhraseQuery, anyWordsQuery=anyWordsQuery, noneWordsQuery=noneWordsQuery, anyHashTagQuery=hashtagQuery, fromAccountsQuery=fromAccountsQuery, toAccountsQuery=toAccountsQuery, mentioningAccountsQuery=mentioningAccountsQuery, minRepliesQuery=minRepliesQuery, minFavesQuery=minFavesQuery, minRTsQuery=minRTsQuery, languageQuery=languagesQuery, toDateQuery=toDateQuery, fromDateQuery=fromDateQuery, repliesFilterQuery=repliesFilterQuery, linksFilterQuery=linksFilterQuery)
    return query.strip()