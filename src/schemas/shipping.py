from marshmallow import Schema, fields

class Dimension(Schema):
    width = fields.Float(required=True)
    height = fields.Float(required=True)

class Payload(Schema):
    dimension = fields.Nested(Dimension, required=True)
    weight = fields.Float(required=True)