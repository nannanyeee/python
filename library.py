class Book: # 한 권의 도서 관리 
    def __init__(self, title, author, isbn, year):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__is_borrowed = False

    # 캡슐화된 접근자(getter)
    def get_title(self): return self.__title
    def get_author(self): return self.__author
    def get_isbn(self): return self.__isbn
    def get_year(self): return self.__year
    def is_borrowed(self): return self.__is_borrowed

    def book_borrowed(self): # 책 대출 메서드 
        if self.__is_borrowed:
            raise Exception(f"'{self.__title}'은 이미 대출 중입니다.")
        self.__is_borrowed = True

    def book_returned(self): # 책 반납 메서드 
        if not self.__is_borrowed:
            raise Exception(f"'{self.__title}'은 대출되지 않았습니다.")
        self.__is_borrowed = False

    def __str__(self):
        status = "대출중" if self.__is_borrowed else "대출 가능"
        return f"[{self.__isbn}] {self.__title} / {self.__author} ({self.__year}) - {status}"


class Member: # 회원, 대출 내역 관리 담당 
    def __init__(self, name):
        self.__name = name 
        self.__borrowed_books = []

    # 캡슐화된 접근자(getter)
    def get_name(self): return self.__name
    def get_borrowed_books(self): return self.__borrowed_books
    
    def member_borrowed(self, book): # 책 대출
        book.book_borrowed()
        self.__borrowed_books.append(book)

    def member_returned(self, book): # 책 반납
        if book in self.__borrowed_books:
            book.book_returned()
            self.__borrowed_books.remove(book)

    def __str__(self):
        return f"회원 {self.__name}"


class Library: # 도서관 
    def __init__(self):
        self.__books = [] # 도서 목록
        self.__members = [] # 회원 목록


    def add_book(self, book): # 도서 추가
        self.__books.append(book)

    def remove_book(self, isbn): # 도서 삭제 
        # 해당 책 객체 찾기 
        target_book = None
        for b in self.__books:
            if b.get_isbn() == isbn:
                target_book = b
                break

        if not target_book:
            print("삭제할 도서를 찾을 수 없습니다.")
                
        # 회원들의 대출 목록에서도 삭제
        for m in self.__members:
            borrowed = m.get_borrowed_books()
            if target_book in borrowed:
                borrowed.remove(target_book)
        print(f"도서 '{target_book.get_title()}' 삭제 완료")
        self.__books = [b for b in self.__books if b.get_isbn() != isbn]



    def search_books(self, keyword, field): # 도서 검색 
        if field == "title":
            return [b for b in self.__books if keyword.lower() in b.get_title().lower()]
        elif field == "author":
            return [b for b in self.__books if keyword.lower() in b.get_author().lower()]
        elif field == "isbn":
            return [b for b in self.__books if keyword == b.get_isbn()]
        else:
            return []

    def register_member(self, member): # 회원 등록 
        self.__members.append(member)

    def find_member(self, member_name): # 회원 검색
        for m in self.__members:
            if m.get_name() == member_name:
                return m
        return None
    
    def library_borrow(self, member_name, isbn): # 도서 대출
        member = self.find_member(member_name)
        if not member:
            raise Exception("회원이 존재하지 않습니다.")
        for book in self.__books:
            if book.get_isbn() == isbn:
                member.member_borrowed(book)
                return f"{book.get_title()} 대출 완료"
        raise Exception("책을 찾을 수 없습니다.")
        
    def library_return(self, member_name, isbn): # 도서 반납
        member = self.find_member(member_name)
        if not member:
            raise Exception("회원이 존재하지 않습니다.")
        for book in member.get_borrowed_books():
            if book.get_isbn() == isbn:
                member.member_returned(book)
                return f"{book.get_title()} 반납 완료"
        raise Exception("해당 책은 이 회원이 빌린 책이 아닙니다.")

    def show_member_loans(self, member_name): # 회원별 대출 현황 확인
        member = self.find_member(member_name)
        if not member:
            raise Exception("회원이 존재하지 않습니다.")
        books = member.get_borrowed_books()
        if not books:
            return f"{member.get_name()} 님은 현재 대출한 책이 없습니다."
        return f"{member.get_name()} 님의 대출 목록:\n" +"\n".join(str(b) for b in books)


def main():
    lib = Library()

    while True:
        print("\n=== 도서관 관리 시스템 ===")
        print("0. 종료")
        print("1. 도서 추가")
        print("2. 도서 삭제")
        print("3. 도서 검색")
        print("4. 회원 등록")
        print("5. 도서 대출")
        print("6. 도서 반납")
        print("7. 회원 대출 현황 확인")

        choice = input("선택: ")

        if choice == "1": # 도서 추가
            title = input("제목: ")
            author = input("저자: ")
            isbn = input("ISBN: ")
            year = int(input("출판연도: "))
            book = Book(title, author, isbn, year)
            lib.add_book(book)
            print("도서 추가 완료")

        elif choice == "2": # 도서 삭제
            isbn = input("삭제할 ISBN: ")
            lib.remove_book(isbn)
            print("도서 삭제 완료")

        elif choice == "3": # 도서 검색(제목, 저자, ISBN으로)
            keyword = input("검색 키워드: ")
            field = input("검색 기준(title/author/isbn): ")
            results = lib.search_books(keyword, field)
            print("검색 결과:")
            for b in results:
                print(b)

        elif choice == "4": # 회원 등록
            name = input("회원 이름: ")
            member = Member(name)
            lib.register_member(member)
            print("회원 등록 완료")

        elif choice == "5": # 도서 대출
            member_name = input("회원 이름: ")
            isbn = input("대출할 ISBN: ")
            try:
                print(lib.library_borrow(member_name, isbn))
            except Exception as e:
                print("오류:", e)


        elif choice == "6": # 도서 반납
            member_name = input("회원 이름: ")
            isbn = input("반납할 ISBN: ")
            try:
                print(lib.library_return(member_name, isbn))
            except Exception as e:
                print("오류:", e)

        elif choice == "7": # 회원 대출 현황 확인
            member_name = input("회원 이름: ")
            try:
                print(lib.show_member_loans(member_name))
            except Exception as e:
                print("오류:", e) 

        elif choice == "0":
            print("프로그램 종료")
            break

        else:
            print("잘못된 번호입니다.")

if __name__ == "__main__":
    main()