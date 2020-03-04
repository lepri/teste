import pytest

from partiu.models import User, Transaction


@pytest.mark.django_db
def test_user_create():
    user = User(email='email@gmail.com', password='password')
    user.save()

    assert User.objects.count() == 1
    assert User.objects.first().email == 'email@gmail.com'


@pytest.mark.django_db
def test_transaction_create(create_user):
    user = create_user()
    transaction = Transaction(user=user, type='exit', value=10)
    transaction.save()

    assert Transaction.objects.count() == 1
    assert Transaction.objects.first().type == 'exit'
