from django.urls import path
from officer.views import *

app_name = 'officer'
urlpatterns = [
    path('', officer_home, name='officer_home'),
    path('officer_login/', officer_login, name='officer_login'),
    path('officer_logout/', officer_logout, name='officer_logout'),
    path('view_complaints/', view_complaints, name='view_complaints'),
    path('complaint_edit/<int:cid>', complaint_edit, name='complaint_edit'),
    path('save_edit/<int:cid>', save_edit, name='save_edit'),
]