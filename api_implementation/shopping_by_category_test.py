import pytest
import json

from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_percentage_discount(client):
    data = [
        {
            'code': '17283640',
            'name': 'Milk',
            'category': 'Food',
            'price': 2.15,
            'quantity': 1,
            'percentage_discount': 10
        }
    ]
    response = client.post('/shopping-statistics/category', json=data)


    assert response.status_code == 200
    assert response.json['Food'] == round(data[0]['price'] * (1-(data[0]['percentage_discount']/100)), 2)


def test_quantity(client):
    data = [
        {
            'code': '17283640',
            'name': 'Milk',
            'category': 'Food',
            'price': 2.15,
            'quantity': 10,
            'percentage_discount': 0
        }
    ]
    response = client.post('/shopping-statistics/category', json=data)

    assert response.status_code == 200
    assert response.json['Food'] == data[0]['price'] * data[0]['quantity']


def test_grouping_by_category(client):
    data = [
        {
            'code': '17283640',
            'name': 'Milk',
            'category': 'Food',
            'price': 2.15,
            'quantity': 4,
            'percentage_discount': 10
        },
        {
            'code': '01827395',
            'name': 'Bread',
            'category': 'Food',
            'price': 5.30,
            'quantity': 2,
            'percentage_discount': 0
        },
    ]
    response = client.post('/shopping-statistics/category', json=data)

    milk_price = (data[0]['price'] * (1-(data[0]['percentage_discount']/100)))*data[0]['quantity']
    bread_price = (data[1]['price'] * (1-(data[1]['percentage_discount']/100)))*data[1]['quantity']

    assert response.status_code == 200
    assert response.json['Food'] == round(milk_price+bread_price, 2)
