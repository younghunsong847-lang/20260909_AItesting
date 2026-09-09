import random

def number_guessing_game():
    """1부터 100 사이의 숫자를 맞추는 게임"""
    # 1부터 100 사이의 임의의 숫자 생성
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("=" * 40)
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")
    print("=" * 40)
    
    while not guessed:
        try:
            # 사용자 입력 받기
            guess = int(input("\n숫자를 입력하세요 (1~100): "))
            attempts += 1
            
            # 입력 범위 확인
            if guess < 1 or guess > 100:
                print("❌ 1부터 100 사이의 숫자를 입력해주세요!")
                continue
            
            # 정답 확인
            if guess == secret_number:
                guessed = True
                print(f"\n🎉 정답입니다! 숫자는 {secret_number}였습니다!")
                print(f"🏆 총 {attempts}번 시도했습니다.")
            elif guess < secret_number:
                print(f"⬆️  입력한 숫자({guess})보다 더 큰 숫자입니다.")
            else:
                print(f"⬇️  입력한 숫자({guess})보다 더 작은 숫자입니다.")
        
        except ValueError:
            print("❌ 유효한 숫자를 입력해주세요!")
    
    # 게임 다시 시작 여부 확인
    while True:
        play_again = input("\n다시 플레이하시겠습니까? (y/n): ").lower()
        if play_again == 'y':
            number_guessing_game()
            break
        elif play_again == 'n':
            print("\n게임을 종료합니다. 즐거운 시간이었습니다! 👋")
            break
        else:
            print("❌ 'y' 또는 'n'을 입력해주세요.")

if __name__ == "__main__":
    number_guessing_game()
