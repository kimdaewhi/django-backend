import requests
from django.shortcuts import render
from django.http import HttpResponse

from member.models import Member
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 1. Key, Secret 코드를 기반으로 요청 url 생성
        key = request.POST.get('app_key', '')  # txt_token 필드에서 입력된 값을 가져옵니다.
        secret = request.POST.get('app_secret', '')
        
        api_url = 'https://openapivts.koreainvestment.com:29443/oauth2/tokenP'
        data = {
            'grant_type': 'client_credentials',
            'appkey': key,
            'appsecret': secret
        }
        response = requests.post(api_url, json=data)
        
        if response.status_code == 200:
            api_response = response.json()
            
            # API 응답을 기반으로 처리
            context = {
                'key': key,
                'secret': secret,
                'api_response': api_response,
            }
            
            # 1. Member Model 객체 생성
            access_token = api_response.get('access_token')
            expired_date = api_response.get('access_token_token_expired')
            token_type = api_response.get('token_type')
            expires_in = api_response.get('expires_in')
            
            member = Member(
                loginId = key,
                access_token = access_token,
                expired_date = expired_date,
                access_token_type = token_type,
                expires_in = expires_in
            )
            
            print(member)
            
            return render(request, 'AutoTradingApp/main.html', context)
        else:
            # API 요청 실패 시 처리
            error_message = response.text
            return HttpResponse(f'<h2>API 요청 실패</h2> {error_message}', status=400)
    
    return render(request, 'AutoTradingApp/login.html')