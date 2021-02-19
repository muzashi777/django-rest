# from django.urls import path
# from snippets import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogs import views

urlpatterns = [
    path('blogs/', views.ArticleList.as_view()),
    path('blogs/<int:pk>/', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
