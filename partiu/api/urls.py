from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from partiu.api import views

router = DefaultRouter()
router.register(r'transaction', views.TransactionViewSet)

urlpatterns = [
    path('v1/users/', views.UserView.as_view()),
    path('v1/user/transaction/<int:user_id>', views.UserTransactionView.as_view()),
    path('v1/user/balance/<int:user_id>', views.UserBalanceView.as_view()),
    path('v1/user/information/<int:pk>', views.UserView.as_view()),
    path('v1/', include(router.urls)),
]
