from marshmallow import fields as models, Schema


class BookSchema(Schema):
    id = models.Integer(required=True)
    title = models.Str(required=True)