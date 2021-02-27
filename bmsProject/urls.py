from django.urls import path, include
from django.contrib import admin
from register import views as v
from chat.views import homepage_view
from register.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('chat/', include('chat.urls', namespace='chat')),
    path('', homepage_view),
    path('', include('django.contrib.auth.urls'))
]
