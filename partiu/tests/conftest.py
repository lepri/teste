import uuid

import pytest

from partiu.models import Transaction


@pytest.fixture
def password():
   return 'some_password'


@pytest.fixture
def create_user(db, django_user_model, password):
    def make_user(**kwargs):
        kwargs['password'] = password
        if 'email' not in kwargs:
            kwargs['email'] = "{}@gmail.com".format(str(uuid.uuid4()))
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def create_transaction(db, create_user):
    def make_transaction(**kwargs):
        if not kwargs['user']:
            kwargs['user'] = create_user()
        transaction = Transaction(**kwargs).save()
        return transaction

    return make_transaction


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()
