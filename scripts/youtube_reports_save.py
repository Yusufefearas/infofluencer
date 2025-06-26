def save_trafficSource_data_to_db(company_id, data):
    from apps.company.models import YouTubeTrafficSourceData
    from django.utils.timezone import now
    
    YouTubeTrafficSourceData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        YouTubeTrafficSourceData.objects.create(
            company_id=company_id,
            date=now().date(),
            insight_traffic_source_type=row["insightTrafficSourceType"],
            views=row["views"],
            average_view_duration=row["averageViewDuration"],
            estimated_minutes_watched=row["estimatedMinutesWatched"]
        )
def save_ageGroup_data_to_db(company_id, data):
    from apps.company.models import YouTubeAgeGroupData
    from django.utils.timezone import now
    
    YouTubeAgeGroupData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        YouTubeAgeGroupData.objects.create(
            company_id=company_id,
            date=now().date(),
            age_group=row["ageGroup"],
            gender=row["gender"],
            viewer_percentage=row["viewerPercentage"]
        )
def save_deviceType_data_to_db(company_id, data):
    from apps.company.models import YouTubeDeviceTypeData
    from django.utils.timezone import now
    
    YouTubeDeviceTypeData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        YouTubeDeviceTypeData.objects.create(
            company_id=company_id,
            date=now().date(),
            device_type=row["deviceType"],
            views=row["views"],
            average_view_duration=row["averageViewDuration"],
            estimated_minutes_watched=row["estimatedMinutesWatched"]
        )
def save_topSubscribers_data_to_db(company_id, data):
    from apps.company.models import YouTubeTopSubscribersData
    from django.utils.timezone import now
    
    YouTubeTopSubscribersData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        YouTubeTopSubscribersData.objects.create(
            company_id=company_id,
            date=now().date(),
            video_id=row["video"],
            subscribers_gained=row["subscribersGained"],
            subscribers_lost=row["subscribersLost"],
            views=row["views"]
        )
