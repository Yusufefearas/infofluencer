from logging import config
import os
from django.shortcuts import redirect, render
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from django.contrib.auth.decorators import login_required
from .models import GA4Token, YouTubeToken
import requests
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.oauth2.credentials import Credentials
import secrets
from .models import OAuthState,GA4AgeData
from django.contrib import messages
from django.contrib.auth import logout,login
from google_auth_oauthlib.flow import Flow
from scripts import ga4_reports as script
from scripts import youtube_scripts
from apps.accounts.models import CompanyProfile
from scripts import ga4_reports_save
from django.http import JsonResponse
from django.db import connection
from apps.company.models import (
    GA4Token,
    YouTubeToken,
    OAuthState,
    GA4AgeData,
    GA4GenderData,
    GA4UserAcquisitionSourceData,
    GA4SessionSourceMediumData,
    GA4OperatingSystemData,
    GA4UserGenderData,
    GA4DeviceCategoryData,
    GA4CountryData,
    GA4CityData,
    YouTubeTrafficSourceData,
    YouTubeAgeGroupData,
    YouTubeDeviceTypeData,
    YouTubeTopSubscribersData,
)
import json
from django.utils.timezone import now

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
if settings.DEBUG:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@login_required(login_url='company_login')
def company_dashboard(request):
    
    veri_listesi = [
        'userAcquisitionSource', 'sessionSourceMedium', 'refferer', 'operatingSystem',
        'userGender', 'deviceCategory', 'country', 'city', 'age'
    ]
    youtube_veri_listesi = [
        'trafficSource', 'ageGroup','deviceType','topSubscribers'
    ]
    return render(request, "company/dashboard.html", {
        "veri_listesi": veri_listesi,
        "youtube_veri_listesi": youtube_veri_listesi
    })

@login_required(login_url='company_login')
def match_influencers(request):
    return render(request, "company/match.html")


@login_required
def ga4_auth_start(request):
    flow = Flow.from_client_config(
        settings.GA4_CLIENT_SECRET_DICT,
        scopes=[
            'https://www.googleapis.com/auth/analytics.readonly',
            'openid',
            'https://www.googleapis.com/auth/userinfo.email'
        ],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )

    # Aynı kullanıcı için eski kayıt varsa sil
    OAuthState.objects.filter(user=request.user, provider="ga4").delete()

    # Yeni state’i DB’ye yaz
    OAuthState.objects.create(user=request.user, provider="ga4", state=state)

    print("🧠 Start -> DB'ye yazılan state:", state)
    print("👤 Kullanıcı:", request.user.id)

    return redirect(authorization_url)


@login_required
def ga4_auth_callback(request):
    # 1. Google'dan gelen state
    incoming_state = request.GET.get("state")

    try:
        # 2. Veritabanından state'e karşılık gelen kullanıcıyı bul
        state_record = OAuthState.objects.get(state=incoming_state, provider="ga4")
        user = state_record.user
    except OAuthState.DoesNotExist:
        return render(request, 'company/error.html', {'error': 'Yetkilendirme başlatılmamış veya geçersiz state.'})

    # 3. Debug logları (isteğe bağlı)
    print("🌐 Google'dan gelen state:", incoming_state)
    print("💾 DB'deki state:", state_record.state)
    print("👤 State'e ait user_id:", user.id)

    # 4. Session güncelle – doğru kullanıcıyı tekrar login et
    login(request, user)
    flow = Flow.from_client_config(
        settings.GA4_CLIENT_SECRET_DICT,
        scopes=[
            'https://www.googleapis.com/auth/analytics.readonly',
            'openid',
            'https://www.googleapis.com/auth/userinfo.email'
        ],
        state=incoming_state,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        include_granted_scopes=False  # 🔥 BURASI ÖNEMLİ
    )
    try:
        flow.fetch_token(authorization_response=request.build_absolute_uri())
    except Exception as e:
        return render(request, 'company/dashboard.html', {'error': f'Google yetkilendirme hatası: {str(e)}'})

    credentials = flow.credentials

    # Access token’ı veritabanına yaz
    GA4Token.objects.update_or_create(
        user=request.user,
        defaults={
            'access_token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_expiry': credentials.expiry
        }
    )

    # Kullanılan state’i sil
    OAuthState.objects.filter(user=request.user, provider="ga4").delete()

    messages.success(request, "Google Analytics bağlantısı başarıyla yapıldı!")
    return redirect("company_dashboard")

# 1️⃣ YouTube Yetkilendirme Başlangıcı
@login_required
def youtube_auth_start(request):
    flow = Flow.from_client_config(
        settings.YOUTUBE_CLIENT_SECRET_DICT,
        scopes=[
            'https://www.googleapis.com/auth/youtube.readonly',
            'https://www.googleapis.com/auth/yt-analytics.readonly',
            'openid', 'https://www.googleapis.com/auth/userinfo.email'
        ],
        redirect_uri=settings.YOUTUBE_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        # include_granted_scopes='true',
        prompt='consent'
    )
    # Debug: Session yazılıyor mu diye kontrol!
    print("YT State:", state)
    request.session['yt_state'] = state
    print("YT Session yazıldı:", request.session.get('yt_state'))
    return redirect(authorization_url)

@login_required
def youtube_auth_callback(request):
    state = request.session.get('yt_state')
    if not state:
        print("Callback geldi. Session state:", state)
        print("GET ile gelen state:", request.GET.get('state'))
        return render(request, 'company/error.html', {'error': 'Session hatası: YouTube yetkilendirmesi başlatılmamış veya zaman aşımına uğramış!'})

    flow = Flow.from_client_config(
        settings.YOUTUBE_CLIENT_SECRET_DICT,
        scopes=[
            'https://www.googleapis.com/auth/youtube.readonly',
            'https://www.googleapis.com/auth/yt-analytics.readonly',
            'openid', 'https://www.googleapis.com/auth/userinfo.email'
        ],
        state=state,
        redirect_uri=settings.YOUTUBE_REDIRECT_URI
    )
    try:
        flow.fetch_token(authorization_response=request.build_absolute_uri())
    except Exception as e:
        # Burada traceback'i yazalım:
        import traceback
        traceback_str = traceback.format_exc()
        print("YouTube Callback Hata Traceback:\n", traceback_str)
        return render(request, 'company/dashboard.html', {
        'error': f'YouTube OAuth Hatası:\n\n{str(e)}\n\nDetaylı Hata:\n{traceback_str}',
        'user': request.user,})

    credentials = flow.credentials
    YouTubeToken.objects.update_or_create(
        user=request.user,
        defaults={
            'access_token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_expiry': credentials.expiry
        }
    )
    return render(request, 'company/dashboard.html', {'user': request.user,'success_message': 'YouTube hesabı başarıyla bağlandı!'})

@login_required
def check_ga4_token(request):
    has_token = GA4Token.objects.filter(user=request.user).exists()
    return JsonResponse({"has_token": has_token})


@csrf_exempt
@login_required
def save_property_id(request):
    if request.method == "POST":
        property_id = request.POST.get("property_id")
        if not property_id:
            return JsonResponse({"error": "Property ID boş olamaz."}, status=400)

        token_obj = GA4Token.objects.get(user=request.user)
        token_obj.property_id = property_id
        token_obj.save()

        return JsonResponse({"status": "kaydedildi"})

    return JsonResponse({"error": "POST olmalı."}, status=405)



import importlib  # ekle

@login_required
def run_custom_report(request):
    veri_tipi = request.GET.get("type")
    if not veri_tipi:
        return JsonResponse({"error": "Veri tipi belirtilmedi."}, status=400)

    print(f"🚨 run_custom_report çağrıldı: veri_tipi={veri_tipi}")

    try:
        token_obj = GA4Token.objects.get(user=request.user)
        property_id = token_obj.property_id

        print(f"🚀 property_id: {property_id}")

        func = getattr(script, f"run_{veri_tipi}_report")
        data = func(
            token_obj.access_token,
            token_obj.refresh_token,
            settings.GOOGLE_CLIENT_ID,
            settings.GOOGLE_CLIENT_SECRET,
            property_id
        )

        print(f"✅ Veri sayısı: {len(data)}")

        # Şimdi CompanyProfile alıyoruz:
        company = CompanyProfile.objects.get(user=request.user)

        # Dinamik olarak save fonksiyonunu çağırıyoruz:
        try:
            save_func_name = f"save_{veri_tipi.lower()}_data_to_db"
            save_func = getattr(importlib.import_module("scripts.ga4_reports_save"), save_func_name)
            save_func(company.id, data)
            print(f"💾 {veri_tipi} data veritabanına kaydedildi.")
        except AttributeError:
            print(f"⚠️ {veri_tipi} için save fonksiyonu bulunamadı, DB kaydı atlanıyor.")

        return JsonResponse({"status": "success", "data": data})

    except AttributeError:
        return JsonResponse({"error": f"{veri_tipi} için fonksiyon bulunamadı."}, status=500)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)
    
@login_required
def run_db_report(request):
    report_type = request.GET.get("type")
    user = request.user

    try:
        company = CompanyProfile.objects.get(user=user)

        if report_type == "age":
            data = list(GA4AgeData.objects.filter(company=company).values('age','active_users','sessions','user_engagement_duration','event_count','conversions'))
        elif report_type == "userAcquisitionSource":
            data = list(GA4UserAcquisitionSourceData.objects.filter(company=company).values('acquisition_source','new_users','sessions','engagement_rate','user_engagement_duration','conversions'))
        elif report_type == "sessionSourceMedium":
            data = list(GA4SessionSourceMediumData.objects.filter(company=company).values('session_source_medium','sessions','conversions','engagement_rate','event_count','bounce_rate'))
        elif report_type == "operatingSystem":
            data = list(GA4OperatingSystemData.objects.filter(company=company).values('operating_system','active_users','engaged_sessions','engagement_rate','user_engagement_duration','event_count','bounce_rate'))
        elif report_type == "userGender":
            data = list(GA4UserGenderData.objects.filter(company=company).values('gender','sessions','engagement_rate','user_engagement_duration','event_count'))
        elif report_type == "deviceCategory":
            data = list(GA4DeviceCategoryData.objects.filter(company=company).values('device_category','active_users','engaged_sessions','user_engagement_duration','event_count','bounce_rate'))
        elif report_type == "country":
            data = list(GA4CountryData.objects.filter(company=company).values('country','active_users','new_users','sessions','user_engagement_duration','event_count','engagement_rate','conversions','bounce_rate'))
        elif report_type == "city":
            data = list(GA4CityData.objects.filter(company=company).values('city','active_users','sessions','user_engagement_duration','event_count','conversions'))
        elif report_type == "trafficSource":
            data = list(YouTubeTrafficSourceData.objects.filter(company=company).values('trafficSource','views','averageViewDuration','estimatedMinutesWatched'))
        elif report_type == "ageGroup":
            data = list(YouTubeAgeGroupData.objects.filter(company=company).values('ageGroup','gender','viewerPercentage'))
        elif report_type == "deviceType":
            data = list(YouTubeDeviceTypeData.objects.filter(company=company).values('deviceType','views','averageViewDuration','estimatedMinutesWatched'))
        elif report_type == "topSubscribers":
            data = list(YouTubeTopSubscribersData.objects.filter(company=company).values('videoID','subscribersGained','subscribersLost','views'))
        else:
            return JsonResponse({"status": "error", "message": "Geçersiz veri tipi"})

        return JsonResponse({"status": "success", "data": data, "type": report_type})

    except CompanyProfile.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Firma profili bulunamadı"})



def company_logout(request):
    logout(request)
    return redirect("home")

@login_required
def get_saved_report_data(request):
    veri_tipi = request.GET.get("type")
    if not veri_tipi:
        return JsonResponse({"error": "Veri tipi belirtilmedi."}, status=400)

    print(f"🚨 get_saved_report_data çağrıldı: veri_tipi={veri_tipi}")

    try:
        company = CompanyProfile.objects.get(user=request.user)

        # Her model için hangi alanları çekeceğini belirle
        model_field_mapping = {
            "trafficSource": {
                "model": YouTubeTrafficSourceData,
                "fields": ['insight_traffic_source_type', 'average_view_duration', 'estimated_minutes_watched']
            },
            "ageGroup": {
                "model": YouTubeAgeGroupData,
                "fields": ['age_group', 'gender', 'viewer_percentage']
            },
            "deviceType": {
                "model": YouTubeDeviceTypeData,
                "fields": ['device_type', 'views', 'average_view_duration', 'estimated_minutes_watched']
            },
            "topSubscribers": {
                "model": YouTubeTopSubscribersData,
                "fields": ['video_id', 'subscribers_gained', 'subscribers_lost', 'views']
            },
        }

        # config değişkenini tanımla
        config = model_field_mapping.get(veri_tipi)
        if not config:
            return JsonResponse({"error": f"{veri_tipi} için model bulunamadı."}, status=400)

        # Model sınıfını al
        ModelClass = config["model"]  # "ModelClass" değil "model"
        
        # Queryset oluştur
        queryset = ModelClass.objects.filter(company_id=company.id)
        data = list(queryset.values(*config["fields"]))

        print(f"✅ DB veri sayısı: {len(data)}")

        return JsonResponse({"status": "success", "data": data})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)
    
import importlib  # En üste ekle

@login_required
def run_youtube_report_view(request):
    report_type = request.GET.get("type")

    youtube_keys = [
        'trafficSource', 'ageGroup', 'deviceType', 'topSubscribers'
    ]

    if report_type not in youtube_keys:
        return JsonResponse({"status": "error", "message": "Geçersiz YouTube raporu"})

    yt_token = request.user.youtubetoken  # access_token, refresh_token vb. modelden gelir

    # 1️⃣ API’den veriyi çek
    result = youtube_scripts.run_youtube_report(
        report_type,
        access_token=yt_token.access_token,
        refresh_token=yt_token.refresh_token,
        client_id=settings.YOUTUBE_CLIENT_ID,
        client_secret=settings.YOUTUBE_CLIENT_SECRET
    )

    # 2️⃣ Dinamik olarak ilgili save fonksiyonunu çağır
    try:
        company = CompanyProfile.objects.get(user=request.user)

        save_func_name = f"save_{report_type}_data_to_db"
        save_func = getattr(importlib.import_module("scripts.youtube_reports_save"), save_func_name)

        save_func(company.id, result)
        print(f"💾 {report_type} raporu veritabanına kaydedildi.")

    except AttributeError:
        print(f"⚠️ {report_type} için save fonksiyonu bulunamadı, DB kaydı atlanıyor.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({
        "status": "success" if isinstance(result, list) else "error",
        "data": result,
        "type": report_type
    })

@login_required
def get_initial_report_status(request):
    company = CompanyProfile.objects.get(user=request.user)
    
    ga4_available = []
    youtube_available = []
    
    # GA4 için sadece city verisi kontrol et
    if GA4CityData.objects.filter(company_id=company.id).exists():
        ga4_available.append("city")
    
    # YouTube için sadece age verisi kontrol et  
    if YouTubeAgeGroupData.objects.filter(company_id=company.id).exists():
        youtube_available.append("ageGroup")
    
    return JsonResponse({
        "status": "success",
        "ga4": ga4_available,
        "youtube": youtube_available
    })