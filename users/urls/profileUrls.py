from django.urls import path

from users import views

urlpatterns = [
    path('profile-form/', views.profileForm, name='profile-form'),
    path('sign-in/', views.signIn, name="sign-in"),
    path('log-out/', views.logoutUser, name="log-out"),

    path('get_school_level_years/', views.getSchoolLevelYears,
         name="get_school_level_years"),
    path('get_talmza_level_years/', views.getTalmzaLevelYears,
         name="get_talmza_level_years"),

    path('profile/search/', views.searchUsers, name="search_users"),
    path('profile/get/<uuid:user_id>/',
         views.getUserProfile, name="get_user_profile"),
]
