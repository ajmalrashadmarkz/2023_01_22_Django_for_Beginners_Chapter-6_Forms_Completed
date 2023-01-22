from django.urls import path
from . import views
# Create your tests here.
urlpatterns = [
    path("test",views.test,name = "test"),
    path("",views.BlogListView.as_view(),name = "post_list"),
    path("post/<int:pk>/",views.BlogDetailView.as_view(),name = "post_detail"),
    path("post/new/",views.BlogCreateView.as_view(),name = "post_create"),
    path("post/<int:pk>/edit/",views.BlogUpdateView.as_view(),name = "post_update"),
    path("post/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="post_delete"),
]