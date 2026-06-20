from django.urls import path
from event_app.views import *

urlpatterns = [
    path('', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    path('dashboard/', dash_board, name='dash_board'),
    path('my-event/', my_event, name='my_event'),
    path('single-event/<str:e_id>/', individual_event, name='individual_event'),
    path('add-event/', add_new_event, name='add_new_event'),
    path('update-event/<str:e_id>', update_event, name='update_event'),
    path('delete-event/<str:e_id>/', delete_event, name='delete_event'),
]
