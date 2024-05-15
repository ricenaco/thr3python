import os
import ast

def ReadData(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r', encoding='UTF-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return {}

def SaveData(data, filename):
    with open(filename, 'w', encoding='UTF-8-sig') as f:
        f.write(str(data))

def SavingsAccount():
    data = ReadData('savings.txt')
    if not data:
        data = {'balance': 0}

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n儲金帳戶管理系統")
        print("===================")
        print("1. 存款")
        print("2. 提款")
        print("3. 顯示餘額")
        print("0. 返回主選單")
        print("===================")

        choice = input("請輸入您的選擇: ")

        if choice == "1":
            amount = float(input("請輸入存款金額: "))
            if amount > 0:
                data['balance'] += amount
                print("已存入 {} 元。".format(amount))
                SaveData(data, 'savings.txt')
            else:
                print("請輸入有效的金額。")
        elif choice == "2":
            amount = float(input("請輸入提款金額: "))
            if 0 < amount <= data['balance']:
                data['balance'] -= amount
                print("已提取 {} 元。".format(amount))
                SaveData(data, 'savings.txt')
            else:
                print("餘額不足或輸入金額無效。")
        elif choice == "3":
            print("帳戶餘額: {:.2f} 元".format(data['balance']))
        elif choice == "0":
            print("返回主選單...")
            break
        else:
            print("請輸入有效的選擇。")
        
        input("按Enter鍵繼續...")

def PersonalFinance():
    transactions = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n個人收支簿程式")
        print("===================")
        print("1. 新增收入")
        print("2. 新增支出")
        print("3. 顯示收支明細")
        print("0. 返回主選單")
        print("===================")

        choice = input("請輸入您的選擇: ")

        if choice == "1":
            amount = float(input("請輸入收入金額: "))
            transactions.append(("收入", amount))
            print("收入 {} 元已記錄。".format(amount))
        elif choice == "2":
            amount = float(input("請輸入支出金額: "))
            transactions.append(("支出", amount))
            print("支出 {} 元已記錄。".format(amount))
        elif choice == "3":
            print("\n收支明細:")
            total_income = total_expense = 0
            for transaction in transactions:
                print("{}: {:.2f} 元".format(transaction[0], transaction[1]))
                if transaction[0] == "收入":
                    total_income += transaction[1]
                else:
                    total_expense += transaction[1]
            print("總收入: {:.2f} 元".format(total_income))
            print("總支出: {:.2f} 元".format(total_expense))
        elif choice == "0":
            print("返回主選單...")
            break
        else:
            print("請輸入有效的選擇。")
        
        input("按Enter鍵繼續...")

def ContactBook():
    contacts = {}

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n客戶通訊錄程式")
        print("===================")
        print("1. 新增客戶")
        print("2. 查詢客戶")
        print("3. 刪除客戶")
        print("0. 返回主選單")
        print("===================")

        choice = input("請輸入您的選擇: ")

        if choice == "1":
            name = input("請輸入客戶姓名: ")
            phone = input("請輸入客戶電話號碼: ")
            email = input("請輸入客戶電子郵件地址: ")
            contacts[name] = {"電話號碼": phone, "電子郵件地址": email}
            print("已新增客戶: {}".format(name))
        elif choice == "2":
            name = input("請輸入要查詢的客戶姓名: ")
            if name in contacts:
                print("\n客戶資訊:")
                print("姓名: {}".format(name))
                print("電話號碼: {}".format(contacts[name]["電話號碼"]))
                print("電子郵件地址: {}".format(contacts[name]["電子郵件地址"]))
            else:
                print("找不到客戶: {}".format(name))
        elif choice == "3":
            name = input("請輸入要刪除的客戶姓名: ")
            if name in contacts:
                del contacts[name]
                print("已刪除客戶: {}".format(name))
            else:
                print("找不到客戶: {}".format(name))
        elif choice == "0":
            print("返回主選單...")
            break
        else:
            print("請輸入有效的選擇。")
        
        input("按Enter鍵繼續...")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n主選單")
        print("===================")
        print("1. 儲金帳戶管理")
        print("2. 個人收支簿程式")
        print("3. 客戶通訊錄程式")
        print("0. 結束程式")
        print("===================")

        choice = input("請輸入您的選擇: ")

        if choice == "1":
            SavingsAccount()
        elif choice == "2":
            PersonalFinance()
        elif choice == "3":
            ContactBook()
        elif choice == "0":
            print("感謝使用，再見！")
            break
        else:
            print("請輸入有效的選擇。")
        
        input("按Enter鍵繼續...")

if __name__ == "__main__":
    main()