#딕셔너리 예제
information = {
    "홍길동": {
        "age": 20,
        "phone": "010-1234-5678",
    },
    "김철수": {
        "age": 22,
        "phone": "010-9876-5432",
    },
    "이영희": {
        "age": 21,
        "phone": "010-1111-2222",
    }
}

while(True):
    print("원하는 기능의 번호를 선택하세요.(1. 연락처 추가 2. 연락처 삭제 3. 연락처 검색 4. 연락처 수정 5. 모든 연락처 보기): ")
    n=int(input())
    if n == 1: #연락처 추가
        name = input("이름 입력: ")
        if name in information:
            print("이미 존재하는 연락처입니다.")
        else:
            age = int(input("나이 입력: "))
            phone = input("전화번호 입력: ")
            information[name] = {"age": age, "phone": phone}
            print(f"{name}의 연락처가 추가되었습니다.")
    elif n == 2: #연락처 삭제
        name = input("이름 입력: ")
        if name in information:
            del information[name]
            print(f"{name}의 연락처가 삭제되었습니다.")
        else:
            print("존재하지 않은 연락처")
    elif n == 3: #연락처 검색
        name = input("이름 입력: ")
        if name in information:
            details = information[name]
            print(f"이름: {name}, 나이: {details['age']}, 전화번호: {details['phone']}")
        else:
            print("존재하지 않은 연락처")
    elif n == 4: #연락처 수정
        if name in information:
            age = int(input("새 나이 입력: "))
            phone = input("새 전화번호 입력: ")
            information[name] = {"age": age, "phone": phone}
            print(f"{name}의 연락처가 수정되었습니다.")
        else:
            print("존재하지 않은 연락처")
    elif n == 5: #모든 연락처 보기
        print("모든 연락처:")
        print("이름\t나이\t전화번호")
        for name, details in information.items():
            print(f"{name}\t{details['age']}\t{details['phone']}")
    else:
        print("잘못된 입력")
        break