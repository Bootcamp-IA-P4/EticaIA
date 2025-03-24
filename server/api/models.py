from pydantic import BaseModel


class Article(BaseModel):
    title: str
    link: str
    topic: str
    excerpt: str | None = None
