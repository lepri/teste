import pytest


TRANSACTION_URL = '/api/v1/transaction/'
USER_TRANSACTION_URL = '/api/v1/user/transaction/'
USER_BALANCE_URL = '/api/v1/user/balance/'
URL_USER_INFORMATION = '/api/v1/user/information/'
URL_USERS_LIST = '/api/v1/users/'


@pytest.mark.django_db
def test_create_transaction_request(api_client, create_user):
    user = create_user(email='user@gmail.com')
    data = {
        'user': user.id,
        'type': 'exit',
        'value': 10
    }

    response = api_client.post(TRANSACTION_URL, type='json', data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_visualize_user_transactions_by_id(api_client, create_transaction, create_user):
    user = create_user()
    create_transaction(user=user, type='entrance', value=10)
    response = api_client.get("{}{}".format(USER_TRANSACTION_URL, user.id))

    assert response.status_code == 200


@pytest.mark.django_db
def test_visualize_user_balance_by_id(api_client, create_transaction, create_user):
    user = create_user()
    create_transaction(user=user, type='entrance', value=10)
    create_transaction(user=user, type='entrance', value=20)
    create_transaction(user=user, type='entrance', value=30)
    create_transaction(user=user, type='exit', value=15)

    response = api_client.get("{}{}".format(USER_BALANCE_URL, user.id))

    assert response.status_code == 200
    assert response.data.get('balance') == 45


@pytest.mark.django_db
def test_visualize_user_data(api_client, create_user):
    user = create_user(email='john.wayne@gmail.com', first_name='John', last_name='Wayne', phone='988884444')

    response = api_client.get("{}{}".format(URL_USER_INFORMATION, user.id))

    assert response.status_code == 200
    assert response.data['email'] == 'john.wayne@gmail.com'
    assert response.data['first_name'] == 'John'
    assert response.data['last_name'] == 'Wayne'
    assert response.data['phone'] == '988884444'


@pytest.mark.django_db
def test_visualize_user_data(api_client, create_user):
    create_user(email='john.wayne@gmail.com', first_name='John', last_name='Wayne', phone='988884444')
    create_user(email='bruce.lee@gmail.com', first_name='Bruce', last_name='Lee', phone='944448888')

    response = api_client.get(URL_USERS_LIST)

    assert response.status_code == 200
    assert len(response.data) == 2

    assert response.data[0]['email'] == 'john.wayne@gmail.com'
    assert response.data[0]['first_name'] == 'John'
    assert response.data[0]['last_name'] == 'Wayne'
    assert response.data[0]['phone'] == '988884444'
