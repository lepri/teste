from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

from partiu.models import Transaction, User
from partiu.api.serializers import TransactionSerializer, UserBalanceSerializer, UserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserTransactionView(generics.ListAPIView):
    """ View to return transaction by user id
    """
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field = 'user_id'

    def get_queryset(self):
        transactions = Transaction.objects.filter(user__id=self.kwargs.get('user_id')).order_by('-created_on')
        return transactions


class UserBalanceView(generics.RetrieveAPIView):
    """ View to return the user balance
    """

    serializer_class = UserBalanceSerializer
    queryset = Transaction.objects.all()
    lookup_field = 'user_id'

    def get(self, request, *args, **kwargs):
        transactions_entrance = Transaction.objects.filter(
            user__id=self.kwargs.get('user_id'), type='entrance'
        ).aggregate(Sum('value'))

        transactions_exit = Transaction.objects.filter(
            user__id=self.kwargs.get('user_id'), type='exit'
        ).aggregate(Sum('value'))

        balance = transactions_entrance['value__sum'] - transactions_exit['value__sum']
        serializer = UserBalanceSerializer({'user': self.kwargs.get('user_id'), 'balance': balance})

        return Response(serializer.data)


class UserView(generics.ListAPIView, generics.RetrieveAPIView):
    """ View to retrieve user and list all users
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
