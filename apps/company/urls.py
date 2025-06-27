from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.company_dashboard,name="company_dashboard"),
    path('google/start/', views.ga4_auth_start, name='ga4_auth_start'),
    path('google/callback/', views.ga4_auth_callback, name='ga4_auth_callback'),
    path('youtube/start/', views.youtube_auth_start, name='youtube_auth_start'),
    path('youtube/callback/', views.youtube_auth_callback, name='youtube_auth_callback'),
    # GA4 entegrasyon adımları
    path("check-ga4-token/", views.check_ga4_token),        # Token var mı?
    path("save-property-id/", views.save_property_id),      # Kullanıcının girdiği property_id'yi kaydet
    path('run-custom-report/', views.run_custom_report, name='run_custom_report'),
    path("logout/", views.company_logout, name="company_logout"),
    path("run-youtube-report/", views.run_youtube_report_view, name="run_youtube_report"),
    path('run-db-report/', views.run_db_report, name='run_db_report'),
    path('get_saved_report_data/', views.get_saved_report_data, name='get_saved_report_data'),
    path("get_initial_report_status/", views.get_initial_report_status, name="get_initial_report_status"),
    path("match/", views.match_influencers, name="match_influencers"),

]