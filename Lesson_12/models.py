from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True, generated=False)
    name = fields.CharField(db_index=True, max_length=255)
    username = fields.CharField(db_index=True, max_length=255, unique=True)
    email = fields.CharField(db_index=True, max_length=255, unique=True)
    comments: fields.ReverseRelation["Comment"]

    def __str__(self):
        return f"{self.__class__.__name__} id = {self.id},username = {self.username!r},email = {self.email!r}"

    def __repr__(self):
        return str(self)


class Post(Model):
    id = fields.IntField(pk=True, generated=False)
    title = fields.CharField(db_index=True, max_length=255),
    body = fields.TextField()
    user_id: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="posts"
    )

    def __str__(self):
        return f"{self.__class__.__name__} id = {self.id},title = {self.title!r}"

    def __repr__(self):
        return str(self)


class Comment(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(db_index=True, max_length=255),
    email = fields.CharField(db_index=True, max_length=255),
    body = fields.TextField()
    post_id: fields.ForeignKeyRelation[Post] = fields.ForeignKeyField(
        "models.Post", related_name="comments"
    )

    def __str__(self):
        return f"{self.__class__.__name__} id = {self.id},name = {self.name!r}"

    def __repr__(self):
        return str(self)