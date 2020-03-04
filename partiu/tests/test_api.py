import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request(api_client):
   url = reverse('transaction/create')
   response = api_client.get(url)
   assert response.status_code == 401
