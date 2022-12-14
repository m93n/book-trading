from django.urls import path, include
from notification import views

urlpatterns = [
    path('create/', views.CreateToken.as_view()),
    path('delete-token/<int:pk>', views.DeleteToken.as_view()),
    path('delete-tokens-by-user/', views.DeleteTokens.as_view()),
    path('tokens', views.ListToken.as_view()),
    path('send-test-massage/' , views.SendTestMessage.as_view() , name = 'send-test-massage') , 
    path('api-auth', include('rest_framework.urls')),
]

