students = {"짱구":50, "철수": 90, "맹구": 70}

while(True):
    print("원하는 기능의 번호를 선택하세요.(1. 학생 추가 2. 학생 삭제 3. 성적 수정 4. 전체 목록 출력 5. 통계 출력): ")
    n=int(input())
    if n == 1: #학생 추가: 이름과 점수를 입력받아 목록에 추가
        name, score = input("이름 점수 입력: ").split()
        students[name] = int(score)
    elif n == 2: #학생 삭제: 이름을 입력받아 해당 학생 정보 삭제
        name = input("이름 입력: ")
        if name in students:
            del students[name]
        else:
            print("존재하지 않은 학생")
    elif n == 3: #성적 수정: 이름을 입력받아 해당 학생의 점수 수정
        name = input("이름 입력: ")
        if name in students:
            score = int(input("새 점수 입력: "))
            students[name] = score
        else:
            print("존재하지 않은 학생")
    elif n == 4: #전체 목록 출력: 모든 학생의 이름과 점수 출력
        print(students.items())
    elif n == 5: #통계 출력: 최고 점수, 최저 점수, 평균 점수 계산 및 출력 
        scores = students.values()
        print(f"최고 점수: {max(scores)}, 최저 점수: {min(scores)}, 평균 점수: {sum(scores)/len(scores)}")
    else:
        print("잘못된 입력")
        break

