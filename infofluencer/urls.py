from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('company/', include('apps.company.urls')),
    path('influencer/', include('apps.influencer.urls')),
    path('', home, name='home'),  # Anasayfa

]
