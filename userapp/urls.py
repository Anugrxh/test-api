from django.urls import path
from .views import UserInfoListCreate, UserInfoDetail,user_page

urlpatterns = [
    path('users/', UserInfoListCreate.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserInfoDetail.as_view(), name='user-detail'),
path('users-page/', user_page, name='users-page'),  # HTML page
]
