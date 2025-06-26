from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from django.conf import settings
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.oauth2.credentials import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.oauth2.credentials import Credentials

def run_userAcquisitionSource_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Dinamik olarak kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="sessionSource")],
        metrics=[
            Metric(name="newUsers"),
            Metric(name="sessions"),
            Metric(name="engagementRate"),
            Metric(name="userEngagementDuration"),
            Metric(name="conversions")
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Acquisition Source": row.dimension_values[0].value,
            "New Users": int(row.metric_values[0].value),
            "Sessions": int(row.metric_values[1].value),
            "Engagement Rate": float(row.metric_values[2].value),
            "Engagement Duration": float(row.metric_values[3].value),
            "Conversions": int(row.metric_values[4].value)
        })

    return data


def run_sessionSourceMedium_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="sessionSourceMedium")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="conversions"),
            Metric(name="engagementRate"),
            Metric(name="eventCount"),
            Metric(name="bounceRate")
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Session Source / Medium": row.dimension_values[0].value,
            "Sessions": int(row.metric_values[0].value),
            "Conversions": int(row.metric_values[1].value),
            "Engagement Rate": float(row.metric_values[2].value),
            "Event Count": int(row.metric_values[3].value),
            "Bounce Rate": float(row.metric_values[4].value)
        })

    return data

def run_refferer_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pageReferrer")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="eventCount"),
            Metric(name="engagementRate"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Referrer": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "Event Count": int(row.metric_values[1].value),
            "Engagement Rate": float(row.metric_values[2].value),
        })

    return data

def run_operatingSystem_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="operatingSystem")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="engagedSessions"),
            Metric(name="engagementRate"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
            Metric(name="bounceRate"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Operating System": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "Engaged Sessions": int(row.metric_values[1].value),
            "Engagement Rate": float(row.metric_values[2].value),
            "User Engagement Duration": float(row.metric_values[3].value),
            "Event Count": float(row.metric_values[4].value),
            "Bounce Rate": float(row.metric_values[5].value),
        })

    return data
def run_userGender_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="userGender")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="engagementRate"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "User Gender": row.dimension_values[0].value,
            "Sessions": int(row.metric_values[0].value),
            "Engagement Rate": int(row.metric_values[1].value),
            "User Engagement Duration": float(row.metric_values[2].value),
            "Event Count": float(row.metric_values[3].value),
        })

    return data
def run_deviceCategory_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="deviceCategory")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="engagedSessions"),
            Metric(name="engagementRate"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
            Metric(name="bounceRate"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Device Category": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "Engaged Sessions": int(row.metric_values[1].value),
            "User Engagement Duration": float(row.metric_values[2].value),
            "Event Count": float(row.metric_values[3].value),
            "Bounce Rate": float(row.metric_values[4].value),
        })

    return data
def run_country_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="newUsers"),
            Metric(name="sessions"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
            Metric(name="engagementRate"),
            Metric(name="conversions"),
            Metric(name="bounceRate"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Country": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "New Users": int(row.metric_values[1].value),
            "Sessions": int(row.metric_values[2].value),
            "User Engagement Duration": float(row.metric_values[3].value),
            "Event Count": float(row.metric_values[4].value),
            "Engagement Rate": float(row.metric_values[5].value),
            "Conversions": float(row.metric_values[6].value),
            "Bounce Rate": float(row.metric_values[7].value),
        })

    return data

def run_city_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
            Metric(name="conversions"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "City": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "Sessions": int(row.metric_values[1].value),
            "User Engagement Duration": float(row.metric_values[2].value),
            "Event Count": float(row.metric_values[3].value),
            "Conversions": float(row.metric_values[4].value),
        })

    return data
def run_age_report(access_token, refresh_token, client_id, client_secret, property_id, token_uri="https://oauth2.googleapis.com/token"):
    # Kimlik bilgilerini oluştur
    creds = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="userAgeBracket")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="userEngagementDuration"),
            Metric(name="eventCount"),
            Metric(name="conversions"),
        ],
        date_ranges=[DateRange(start_date="2025-01-01", end_date="2025-05-27")]
    )

    response = client.run_report(request)

    data = []
    for row in response.rows:
        data.append({
            "Age": row.dimension_values[0].value,
            "Active Users": int(row.metric_values[0].value),
            "Sessions": int(row.metric_values[1].value),
            "User Engagement Duration": float(row.metric_values[2].value),
            "Event Count": float(row.metric_values[3].value),
            "Conversions": float(row.metric_values[4].value),
        })

    return data

