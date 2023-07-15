from django.urls import path
from . import views
#from .views import DescriptionListView

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post_slug>', views.DetaView.as_view(), name='post_detail'),#{% url 'post_detail' m.slug %}
    path('post/<slug:posts_slug>', views.PostDetail.as_view(), name='list_details'),
]
