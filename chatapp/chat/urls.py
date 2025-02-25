from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create/', views.create_group, name='create'),
    path('groups/', views.groups, name='chat_list' ),
    path('groups/<int:id>', views.group_chat, name='group_chat'),
    path('upload/', views.imagePost, name='upload')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)