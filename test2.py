import random

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if user_choice in ['가위', '바위', '보']:
            return user_choice
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        return "사용자 승리"
    else:
        return "컴퓨터 승리"

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("다시 하시겠습니까? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
