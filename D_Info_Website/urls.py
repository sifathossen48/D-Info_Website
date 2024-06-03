from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home_Page.urls')),
    path('about/',include('About_Page.urls')),
    path('termsCondition/', include('TermsCondition.urls')),
    path('returnPolicy/', include('ReturnPolicy.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

