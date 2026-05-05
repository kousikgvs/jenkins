STATIC_CUSTOMER_DATA = [
    {
        'customer_id': 1,
        'name': 'Asha',
        'city': 'hyderabad',
        'age': 29,
        'monthly_spend': 1200.0,
    },
    {
        'customer_id': 2,
        'name': 'Rahul',
        'city': 'mumbai',
        'age': None,
        'monthly_spend': 980.5,
    },
    {
        'customer_id': 3,
        'name': 'Meera',
        'city': 'delhi',
        'age': 35,
        'monthly_spend': 1500.75,
    },
]


def get_static_customer_data():
    return [record.copy() for record in STATIC_CUSTOMER_DATA]