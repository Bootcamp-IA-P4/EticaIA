def article_serializer(article):
    return {
        "_id": str(article["_id"]),
        "title": article["title"],
        "link": article["link"],
        "topic": article["topic"],
    }
