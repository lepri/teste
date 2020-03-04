from rest_framework import serializers

from partiu.models import Transaction, User


class TransactionSerializer(serializers.ModelSerializer):
    """ Serializer for Transaction model
    """

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'type', 'value', 'created_on')
        read_only_fields = ('id',)


class UserBalanceSerializer(serializers.Serializer):
    """ Serializer to return the user balance
    """

    user = serializers.IntegerField()
    balance = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone')
        read_only_fields = ('id',)
