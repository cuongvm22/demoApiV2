from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<productId>\w{0,100})', views.getProduct),
]
