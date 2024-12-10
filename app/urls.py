from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Admin URLs
path("home/admin", AdminHomeView.as_view(), name="admin-home"),
path("register/admin", AdminRegistrationView.as_view(), name="admin-registration"),
path('login/admin', AdminLoginView.as_view(), name='admin-login'),
path('add/locations', AddLocationView.as_view(), name="add-locations"),
path('approval/<int:pk>', approve_mechanic, name="approve"),

# Mechanic URLs
path("mechanic/home", MechnaicHomeView.as_view(), name="mechanic_home"),
path("add/profile/<int:pk>", MechanicProfileAddView.as_view(), name="add-profile"),
path("profile/view/<int:pk>", MechanicProfileDetailView.as_view(), name="view-profile"),
path("profile/<int:pk>/update", MechanicprofileUpdateView.as_view(), name="update-profile"),
path('pending', PendingMechanicView.as_view(), name="pending-list"),
path('my-requests/', MechanicReqListView.as_view(), name='mechanic_requests'),
path('mechanicapproval/<int:pk>', update_status, name="mech-approve"),
path('feedback-list/', FeedbackListView.as_view(), name='feedback_list'),
path('create-bill-payment/<int:pk>/', BillPaymentCreateView.as_view(), name='create_bill_payment'),


# User URLs
path("user/home", UserHomeView.as_view(), name="user_home"),
path("user/registration", RegistrationView.as_view(), name="user_registration"),
path("useradd/profile/<int:pk>", UserProfileAddView.as_view(), name="useradd-profile"),
path("userprofile/view/<int:pk>", UserProfileDetailView.as_view(), name="userview-profile"),
path("userprofile/update/<int:pk>", UserProfileUpdateView.as_view(), name="userupdate-profile"),
path('approved-mechanics/', ApprovedMechanicListView.as_view(), name='approved_mechanics'),
path("create/req/<int:mechanic_id>", ReqToMechanicCreateView.as_view(), name="create_req"),
path('requests/', UserRequestsListView.as_view(), name='user_requests'),
path('feedback/<int:pk>', FeedBackCreateView.as_view(), name='feedback_form'),
path('bill-payment/<int:pk>/', bil_payment, name='bill_payment'),
path('cars/available/', RentCarListView.as_view(), name='available_cars'),
path('reserve/<int:pk>/', ReserveCarView.as_view(), name='reserve_car'),
path('reservations/', UserReservationListView.as_view(), name='user_reservation_list'),
path('update_reservation/<int:pk>/',update_reservation, name='update_reservation'),

#car renter URLS
path("car/home", CarRenterHomeView.as_view(), name="car_home"),
path('car_renter_profile/<int:pk>', CarRenterProfileCreateView.as_view(), name='car_renter_profile'),
path('car_renter_profile/update/<int:pk>', CarRenterProfileUpdateView.as_view(), name='car_renter_profile_update'),
path('car_renter_profile/view/', CarRenterProfileDetailView.as_view(), name='car_renter_profile_view'),
path('rent_car/', RentCarCreateView.as_view(), name='rent_car_create'),
path('rent_car/update/<int:pk>/', RentCarUpdateView.as_view(), name='rent_car_update'),
path('rentcars/', UserRentCarListView.as_view(), name='rentcar_list'),
path('my_reservations/', CarOwnerReservationsListView.as_view(), name='car_owner_reservations'),

# path('reservation/<int:pk>', ReservationDetailView.as_view(), name='reservation_detail'),


# Common URLs
path("",HomeView.as_view(),name="home"),
path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView, name='logout'), 
path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
path("payment/sucess/",PaymentSuccessView.as_view(),name="payment"),
path('search/',mechanic_search, name='mechanic_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
