from marshmallow import Schema, fields

class Dimension(Schema):
    width = fields.Float()
    height = fields.Float()

class Payload(Schema):
    dimension = fields.Nested(Dimension)
    weight = fields.Float()