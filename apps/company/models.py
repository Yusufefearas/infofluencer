from django.db import models
from django.contrib.auth.models import User
from apps.accounts.models import CompanyProfile

class GA4Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expiry = models.DateTimeField()
    property_id = models.CharField(max_length=20, null=True, blank=True)  
    def __str__(self):
        return f"{self.user.username} - GA4 Token"

class YouTubeToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expiry = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - YouTube Token"
class OAuthState(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=255)
    provider = models.CharField(max_length=50)  # 'ga4' veya 'youtube'
    created_at = models.DateTimeField(auto_now_add=True)

class GA4AgeData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    age_group = models.CharField(max_length=50)
    active_users = models.IntegerField()
    sessions = models.IntegerField()
    user_engagement_duration = models.FloatField()
    event_count = models.FloatField()
    conversions = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class GA4GenderData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    age_group = models.CharField(max_length=50)
    active_users = models.IntegerField()
    sessions = models.IntegerField()
    user_engagement_duration = models.FloatField()
    event_count = models.FloatField()
    conversions = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class GA4UserAcquisitionSourceData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    acquisition_source = models.CharField(max_length=255)  # dimension: sessionSource
    new_users = models.IntegerField()
    sessions = models.IntegerField()
    engagement_rate = models.FloatField()
    user_engagement_duration = models.FloatField()
    conversions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4SessionSourceMediumData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    session_source_medium = models.CharField(max_length=255)  # Dimension: sessionSourceMedium
    sessions = models.IntegerField()
    conversions = models.IntegerField()
    engagement_rate = models.FloatField()
    event_count = models.IntegerField()
    bounce_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4OperatingSystemData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    operating_system = models.CharField(max_length=100)  # Dimension: operatingSystem
    active_users = models.IntegerField()
    engaged_sessions = models.IntegerField()
    engagement_rate = models.FloatField()
    user_engagement_duration = models.FloatField()
    event_count = models.IntegerField()
    bounce_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4UserGenderData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    gender = models.CharField(max_length=50)  # Dimension: userGender
    sessions = models.IntegerField()
    engagement_rate = models.FloatField()
    user_engagement_duration = models.FloatField()
    event_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4DeviceCategoryData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    device_category = models.CharField(max_length=50)  # Dimension
    active_users = models.IntegerField()
    engaged_sessions = models.IntegerField()
    user_engagement_duration = models.FloatField()
    event_count = models.IntegerField()
    bounce_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4CountryData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.CharField(max_length=100)  # Dimension
    active_users = models.IntegerField()
    new_users = models.IntegerField()
    sessions = models.IntegerField()
    user_engagement_duration = models.FloatField()
    event_count = models.IntegerField()
    engagement_rate = models.FloatField()
    conversions = models.IntegerField()
    bounce_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
class GA4CityData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    city = models.CharField(max_length=100)  # Dimension
    active_users = models.IntegerField()
    sessions = models.IntegerField()
    user_engagement_duration = models.FloatField()
    event_count = models.IntegerField()
    conversions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
class YouTubeTrafficSourceData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    insight_traffic_source_type = models.CharField(max_length=100)
    views = models.IntegerField()
    average_view_duration = models.FloatField()
    estimated_minutes_watched = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
class YouTubeAgeGroupData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    age_group = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    viewer_percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
class YouTubeDeviceTypeData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    device_type = models.CharField(max_length=50)
    views = models.IntegerField()
    average_view_duration = models.FloatField()
    estimated_minutes_watched = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
class YouTubeTopSubscribersData(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    video_id = models.CharField(max_length=50)
    subscribers_gained = models.IntegerField()
    subscribers_lost = models.IntegerField()
    views = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
