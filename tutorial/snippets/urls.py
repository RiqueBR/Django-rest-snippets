from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
  # function based views
  
  # path('snippets/', views.snippet_list),
  # path('snippets/<int:pk>', views.snippet_detail)

  # class based views
  path('snippets/', views.SnippetList.as_view()),
  path('snippets/<int:pk>', views.SnippetDetail.as_view()),

  # User paths
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>', views.UserDetail.as_view())

]

# enable format switching
urlpatterns = format_suffix_patterns(urlpatterns)