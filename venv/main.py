import feedparser
NewsFeed = feedparser.parse("feed:https://www.gazetaesportiva.com/times/flamengo/feed/")
entry = NewsFeed.entries[1]

print('Number of RSS posts :', len(NewsFeed.entries))

entry = NewsFeed.entries[1]


# get the feed
print(entry.published)
print("******")
print(entry.summary)
print("------News Link--------")
print(entry.link)

# convert to html




