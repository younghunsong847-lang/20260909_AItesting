import requests
import time
import os
from datetime import datetime

# 환율 API (무료 서비스)
API_URL = "https://api.exchangerate-api.com/v4/latest"

# 지원하는 통화
SUPPORTED_CURRENCIES = {
    '1': 'USD',
    '2': 'JPY',
    '3': 'CNY'
}

def clear_screen():
    """화면을 깨끗이 지우기"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_exchange_rate(base_currency, target_currencies):
    """실시간 환율 정보 조회"""
    try:
        response = requests.get(f"{API_URL}/{base_currency}", timeout=5)
        response.raise_for_status()
        data = response.json()
        
        rates = {}
        for currency in target_currencies:
            if currency in data.get('rates', {}):
                rates[currency] = data['rates'][currency]
        
        return rates, data.get('time_last_updated')
    except requests.exceptions.RequestException as e:
        return None, None

def display_exchange_rate(base_currency, rates, timestamp):
    """환율 정보 표시"""
    print(f"\n📊 환율 정보")
    print("=" * 50)
    print(f"기준 통화: {base_currency} (한국 원화)")
    print(f"마지막 업데이트: {datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    for currency, rate in rates.items():
        currency_names = {
            'USD': '미국 달러',
            'JPY': '일본 엔',
            'CNY': '중국 위안'
        }
        print(f"{currency} ({currency_names.get(currency, currency)}) : {rate:,.4f}")
    print("=" * 50)

def select_currency():
    """사용자로부터 통화 선택받기"""
    print("\n원하는 통화를 선택하세요:")
    print("1. USD (미국 달러)")
    print("2. JPY (일본 엔)")
    print("3. CNY (중국 위안)")
    print("0. 종료")
    
    while True:
        choice = input("\n선택 (0-3): ").strip()
        if choice in ['0', '1', '2', '3']:
            return choice
        print("❌ 0부터 3 사이의 숫자를 입력해주세요!")

def main():
    """메인 함수"""
    print("=" * 50)
    print("💱 실시간 환율 조회 애플리케이션")
    print("=" * 50)
    print("※ 기준 통화: KRW (한국 원화)")
    
    choice = select_currency()
    
    if choice == '0':
        print("\n앱을 종료합니다. 👋")
        return
    
    target_currency = SUPPORTED_CURRENCIES[choice]
    
    print(f"\n✅ {target_currency} 환율 조회를 시작합니다.")
    print("30초마다 최신 환율을 업데이트합니다.")
    print("Ctrl+C를 눌러 종료할 수 있습니다.\n")
    
    update_count = 0
    
    try:
        while True:
            update_count += 1
            print(f"[업데이트 #{update_count}] {datetime.now().strftime('%H:%M:%S')}")
            
            rates, timestamp = get_exchange_rate('KRW', [target_currency])
            
            if rates and timestamp:
                display_exchange_rate('KRW', rates, timestamp)
                print(f"\n다음 업데이트까지 30초 대기 중...\n")
            else:
                print("❌ 환율 정보를 불러올 수 없습니다.")
                print("인터넷 연결을 확인해주세요.\n")
            
            # 30초 대기
            time.sleep(30)
    
    except KeyboardInterrupt:
        print("\n\n앱을 종료합니다. 👋")
        print(f"총 {update_count}회 업데이트했습니다.")

if __name__ == "__main__":
    main()
