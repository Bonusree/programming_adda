from django.urls import path
from problems import views 


urlpatterns = [
    path('problems/',views.problems, name='problems'),
    path('problems/addproblem/',views.addproblem, name='addproblem'),
    path('problems/filter-problem/', views.filterProblem, name='filter_problem'),
    path('search-suggestion/',views.searchSuggestion,name='searchSuggestion'),
    path('new-tag-suggestion/',views.newTagSuggestion,name='newtagsuggestion'),
]
