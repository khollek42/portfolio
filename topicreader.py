import pandas


def topics():
    topiclist = []

    topics = pandas.read_csv("topics.csv")

    for topic in topics["Topics"]:
        topiclist.append(topic)

    return topiclist