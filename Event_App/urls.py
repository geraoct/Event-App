from django .urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[

    path('', views.Home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('Add_Event/', views.create_event, name='add_event'),
    path('Event_List/', views.event_list_view, name='event_list'),
    path('Delete_Event/<int:event_id>/', views.delete_event_view, name='delete_event'),
    path('Edit_Event/<int:event_id>/', views.edit_event_view, name='event_edit'),
    path('Events_Detail/<int:event_id>/', views.events_view, name='my_events_view'),
    path('Upcoming_Events/', views.upcoming_events_view, name='upcoming_events'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)