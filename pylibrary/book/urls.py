from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<slug:book_slug>', cache_page(60)(views.BookDetailView.as_view()), name='book_info'),
    path('category/<slug:category_slug>', views.CategoryInfoView.as_view(), name='category_info'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add_review'),
    path('create/', views.AddCrateView.as_view(), name='create'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete'),
]
