if __name__ == '__main__':
    import jiagu

    text = '很讨厌还是个懒鬼'
    sentiment = jiagu.sentiment(text)
    print(sentiment)