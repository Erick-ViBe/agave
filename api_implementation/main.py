from flask import Flask, request
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app)


shopping_fields = api.model('Shopping', {
    'code': fields.String(required=True),
    'name': fields.String(required=True),
    'category': fields.String(required=True),
    'price': fields.Float(required=True),
    'quantity': fields.Integer(required=True),
    'percentage_discount': fields.Float(required=True),
})


@api.route('/shopping-statistics/category', endpoint='shopping-by-category')
class ShoppingByCategory(Resource):
    @api.expect([shopping_fields], validate=True)
    def post(self):
        shopping_list = request.get_json()
        shopping_by_category = {}

        for shopping in shopping_list:
            discounted_price = shopping['price'] * (1-(shopping['percentage_discount']/100))
            shopping_price = round(discounted_price+shopping_by_category.get(shopping['category'], 0), 2)
            shopping_by_category[shopping['category']] = shopping_price

        return shopping_by_category
