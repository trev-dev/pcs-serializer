import json


class CommentJSONFilter:

    """
    Creates a prepared JSON list of comments in the
    form of a filter for Vue components
    """

    def __init__(self, comments):
        self.comments = comments
        self.prepared_list = []

    def _extract_comment(self, c):
        data = {
            'date': c.locale_date,
            'author': c.author.name,
            'url': c.url,
            'slug': c.slug,
            'content': c.content,
            'email': c.email,
        }

        if c.replies:
            data['replies'] = [
                self._extract_comment(com) for com in c.replies
            ]

        return data

    def _iterate_comments(self):
        for c in self.comments:
            self.prepared_list.append(self._extract_comment(c))

    def run(self):
        self._iterate_comments()
        return json.dumps(self.prepared_list)
