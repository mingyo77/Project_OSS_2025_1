import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
    def search_expenses(self, keyword):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
    
        results = [e for e in self.expenses if keyword in e.category or keyword in e.description]
        if not results:
            print(f"'{keyword}'에 해당하는 지출 내역이 없습니다.\n")
            return

        print(f"\n[검색 결과: '{keyword}']")
        for idx, e in enumerate(results, 1):
            print(f"{idx}. {e}")
        print()    

