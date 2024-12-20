from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from myapp.views import (
    hello,
    index,
    about,
    feedback,
    report_crime,
    services,
    mwanted,
    submit_user_info,
    indexdashboard,
    openreports,
    resolvedreports,
    totalreports,
    notifications,
    requestreport,
    loginform,
    otp_verification,
)

urlpatterns = [
    path('hello/', hello, name='hello'),  # Hello endpoint
    path('', index, name='index'),        # Home page
    path('about/', about, name='about'),  # About page
    path('feedback/', feedback, name='feedback'),  # Contact page
    path('report_crime/', report_crime, name='report_crime'),  # Report Crime page
    path('services/', services, name='services'),  # Services page
    path('submit-user-info/', submit_user_info, name='submit_user_info'),  # User Info submission URL
    path('indexdashboard/', indexdashboard, name='indexdashboard'),  # Dashboard
    path('openreports/<int:id>/', openreports, name='openreports'),  # Open a specific report
    path('resolvedreports/', resolvedreports, name='resolvedreports'),  # Resolved reports
    path('totalreports/', totalreports, name='totalreports'),  # Total reports
    path('notifications/', notifications, name='notifications'),  # Notifications
    path('requestreport/', requestreport, name='requestreport'),  # Request report
    path('loginform/', loginform, name='loginform'),  # Login form
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('mwanted/', mwanted, name='mwanted'),  # Most Wanted page
    path('otp_verification/', otp_verification, name='otp_verification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)