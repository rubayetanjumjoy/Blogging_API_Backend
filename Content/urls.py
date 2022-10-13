from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .apis import *

urlpatterns = [

    path('blog/', BlogList.as_view(), name='bloglist'),
    path('blog/<int:pk>', BlogView.as_view(), name='bloglist'),
    path('search/', SearchBlog.as_view(), name='search'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
