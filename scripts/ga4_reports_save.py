# scripts/ga4_reports_save.py

from apps.company.models import (
    GA4AgeData,
    GA4UserAcquisitionSourceData,
    GA4SessionSourceMediumData,
    GA4OperatingSystemData,
    GA4UserGenderData,
    GA4DeviceCategoryData,
    GA4CountryData,
    GA4CityData,
)
from django.utils.timezone import now

def save_age_data_to_db(company_id, data):
    # Eski veriyi sil (isteğe bağlı)
    GA4AgeData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4AgeData.objects.create(
            company_id=company_id,
            date=now().date(),
            age_group=row["Age"],
            active_users=row["Active Users"],
            sessions=row["Sessions"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"],
            conversions=row["Conversions"]
        )
def save_useracquisitionsource_data_to_db(company_id, data):
    GA4UserAcquisitionSourceData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4UserAcquisitionSourceData.objects.create(
            company_id=company_id,
            date=now().date(),
            acquisition_source=row["Acquisition Source"],
            new_users=row["New Users"],
            sessions=row["Sessions"],
            engagement_rate=row["Engagement Rate"],
            user_engagement_duration=row["Engagement Duration"],
            conversions=row["Conversions"]
        )
def save_sessionsourcemedium_data_to_db(company_id, data):
    GA4SessionSourceMediumData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4SessionSourceMediumData.objects.create(
            company_id=company_id,
            date=now().date(),
            session_source_medium=row["Session Source / Medium"],
            sessions=row["Sessions"],
            conversions=row["Conversions"],
            engagement_rate=row["Engagement Rate"],
            event_count=row["Event Count"],
            bounce_rate=row["Bounce Rate"]
        )
def save_operatingsystem_data_to_db(company_id, data):
    GA4OperatingSystemData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4OperatingSystemData.objects.create(
            company_id=company_id,
            date=now().date(),
            operating_system=row["Operating System"],
            active_users=row["Active Users"],
            engaged_sessions=row["Engaged Sessions"],
            engagement_rate=row["Engagement Rate"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"],
            bounce_rate=row["Bounce Rate"]
        )
def save_usergender_data_to_db(company_id, data):
    GA4UserGenderData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4UserGenderData.objects.create(
            company_id=company_id,
            date=now().date(),
            gender=row["User Gender"],
            sessions=row["Sessions"],
            engagement_rate=row["Engagement Rate"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"]
        )
def save_usergender_data_to_db(company_id, data):
    GA4UserGenderData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4UserGenderData.objects.create(
            company_id=company_id,
            date=now().date(),
            gender=row["User Gender"],
            sessions=row["Sessions"],
            engagement_rate=row["Engagement Rate"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"]
        )
def save_devicecategory_data_to_db(company_id, data):
    GA4DeviceCategoryData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4DeviceCategoryData.objects.create(
            company_id=company_id,
            date=now().date(),
            device_category=row["Device Category"],
            active_users=row["Active Users"],
            engaged_sessions=row["Engaged Sessions"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"],
            bounce_rate=row["Bounce Rate"]
        )
def save_country_data_to_db(company_id, data):
    GA4CountryData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4CountryData.objects.create(
            company_id=company_id,
            date=now().date(),
            country=row["Country"],
            active_users=row["Active Users"],
            new_users=row["New Users"],
            sessions=row["Sessions"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"],
            engagement_rate=row["Engagement Rate"],
            conversions=row["Conversions"],
            bounce_rate=row["Bounce Rate"]
        )
def save_city_data_to_db(company_id, data):
    GA4CityData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4CityData.objects.create(
            company_id=company_id,
            date=now().date(),
            city=row["City"],
            active_users=row["Active Users"],
            sessions=row["Sessions"],
            user_engagement_duration=row["User Engagement Duration"],
            event_count=row["Event Count"],
            conversions=row["Conversions"]
        )
def save_referrer_data_to_db(company_id, data):
    GA4ReferrerData.objects.filter(company_id=company_id, date=now().date()).delete()

    for row in data:
        GA4ReferrerData.objects.create(
            company_id=company_id,
            date=now().date(),
            page_referrer=row["Referrer"],
            active_users=row["Active Users"],
            event_count=row["Event Count"],
            engagement_rate=row["Engagement Rate"]
        )
