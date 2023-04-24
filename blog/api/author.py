from combojsonapi.event.resource import EventsResource

from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import Author, Article


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {
            "count": Article.query.filter(Article.author_id == kwargs["id"]).count()
        }


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
