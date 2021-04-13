from typing import List, Optional

from pydantic import BaseModel

class ItunesAttrs(BaseModel):
    href: str

class Itunes(BaseModel):
    content: str
    attrs: Optional[ItunesAttrs]

class EnclosureAttrs(BaseModel):
    url: str
    length: int
    type: str

class Enclosure(BaseModel):
    content: str
    attrs: Optional[EnclosureAttrs]

class DescriptionImage(BaseModel):
    alt: Optional[str]
    source: str

class FeedItem(BaseModel):
    title: str
    link: str
    publish_date: Optional[str]
    category: Optional[str]
    description: str
    description_links: Optional[List[str]]
    description_images: Optional[List[DescriptionImage]]
    enclosure: Optional[Enclosure]
    itunes: Optional[Itunes]

    # https://stackoverflow.com/questions/10994229/how-to-make-an-object-properly-hashable#answer-38259091
    # added this, so you can call/use in a set() on the FeedItem's to ensure no duplicates in a list.
    def __hash__(self):
        return hash(self.title.strip())

    def __eq__(self,other):
        return self.title.strip() == other.title.strip()

class RSSFeed(BaseModel):
    title: str
    version: Optional[str]
    language: Optional[str]
    description: Optional[str]
    feed: List[FeedItem]