import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
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
        
            return render(request, 'member/main.html', context)
        else:
            # API 요청 실패 시 처리
            error_message = response.text
            return HttpResponse(f'API 요청 실패: {error_message}', status=400)
    
    return render(request, 'member/login.html')