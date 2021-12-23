from django.urls import path, include
from rest_framework import routers

from partner import views

router = routers.DefaultRouter()
# router.register('parterdata', ParterViewSet)
urlpatterns = [
    path('partner-list/', views.PartnerList.as_view()),
    path('partner-list/<int:pk>', views.PartnerDetail.as_view()),
    path('data-sharing/', views.DataSharingList.as_view()),
    path('data-sharing/<int:pk>',views.DataSharingUpdate.as_view()),
    path('data-document/',views.DataSharingDocumentPost.as_view()),
    path('data-document/<int:pk>', views.DataSharingDocumentUpdate.as_view()),
    path('contact-list/',views.ContactList.as_view()),
    path('contact-list/<int:pk>',views.ContactUpdate.as_view())
]