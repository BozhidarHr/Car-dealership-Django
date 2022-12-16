from django.urls import path

from car_dealer.web.views import home_view, register_view, login_view, logout_view, listing_view, DeleteListingView, \
    FeedbackView, EditListingView, MyListingsView, ContactUsView, ReportListingView, detail_view

urlpatterns = (
    path('', home_view, name='home'),
    path('login/', login_view, name="login form"),
    path('register/', register_view, name='registration form'),
    path('logout/', logout_view, name='logout'),
    path('create_listing/', listing_view, name='create listing'),
    path('delete/<int:pk>', DeleteListingView.as_view(), name='delete listing'),
    path('edit/<int:pk>', EditListingView.as_view(), name='edit listing'),
    path('details/<int:pk>', detail_view, name='detailed listing'),
    path('feedback/', FeedbackView.as_view(),name='feedback view'),
    path('my_listings/', MyListingsView.as_view(), name='my listings view'),
    path('contact/', ContactUsView.as_view(), name='contact us'),
    path('report/<int:pk>', ReportListingView.as_view(), name='report listing')
)