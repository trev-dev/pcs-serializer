from pelican import signals
from .jsonfilter import CommentJSONFilter


def serialize(cls):
    serializer = CommentJSONFilter(cls)
    data = serializer.run()
    return data


def add_filter(pelican):
    pelican.env.filters.update({'cserializer': serialize})


def register():
    signals.generator_init.connect(add_filter)
