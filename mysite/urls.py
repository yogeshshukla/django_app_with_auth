from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
