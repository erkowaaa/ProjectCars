from django.urls import path
from .views import *


urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/',CarViewSet.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='car_detail'),

    path('user/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='users_detail'),

    path('auction/', AuctionViewSet.as_view({'get': 'list', 'post': 'create'}), name='auctions_list'),
    path('auction/<int:pk>/', AuctionViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'}), name='auctions_detail'),

    path('bid/', BidViewSet.as_view({'get': 'list', 'post': 'create'}), name='bids_list'),
    path('bid/<int:pk>/', BidViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='bids_detail'),

    path('feedback/', FeedbackViewSet.as_view({'get': 'list', 'post': 'create'}), name='feedbacks_list'),
    path('feedback/<int:pk>/', FeedbackViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name='feedbacks_detail'),
]