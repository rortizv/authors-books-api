from django.contrib import admin
from django.urls import path,include
from bookreview import views
from bookreview.views import AuthorInstanceView


urlpatterns = [
    path('', views.AuthorView.as_view(), name='author-list'),
    path('admin/', admin.site.urls),
    path('books/', include('bookreview.urls')),
    path('authors/<int:pk>', AuthorInstanceView.as_view(), name='author-instance')
]