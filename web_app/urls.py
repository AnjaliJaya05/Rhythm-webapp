from django.urls import path
from .views import *


urlpatterns=[
    path('index/',index),
    path('reg/',reg),
    path('log/',log),
    path('adminlogin/',adminlogin),
    path('alog/',alog),
    path('index1/',index1),
    path('addpro/',add_pro),
    path('pro_display/',pro_display),
    path('pro_del/<int:id>',pro_del),
    path('pro_edit/<int:id>',pro_edit),
    path('wish/<int:id>',wish),
    path('wishdisplay/',wishdisplay),
    path('wish_rem/<int:id>',wish_rem),
    path('cart/<int:id>',cart),
    path('cartdisplay/',cartdisplay),
    path('cart_rem/<int:id>',cart_rem),
    path('profile/',profile),
    path('edit/<int:id>',edit),
    path('logout/',logout_view),
    path('change/<int:id>',change),
    path('forgot/',forgot_password),
    path('check/<int:id>',check),
    path('card',card),
    path('success/',success),

]