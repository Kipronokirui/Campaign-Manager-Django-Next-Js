from django.urls import path
from .views import CampaignListAPIView, CampaignDetailAPIView, SubscribeToCampaignAPIView

urlpatterns=[
    path('campaigns', CampaignListAPIView.as_view(), name='campaigns'),
    path('campaign/<str:slug>', CampaignDetailAPIView.as_view(), name='campaign'),
    path('campaign/subscribe', SubscribeToCampaignAPIView.as_view(), name='subscribe'),
]