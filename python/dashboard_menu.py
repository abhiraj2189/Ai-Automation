import os

def main():
    while True:

        print("\n" + "=" * 60)
        print("         AI AUTOMATION DASHBOARD")
        print("=" * 60)

        print("1. GitHub Module")
        print("2. AI Tools Module")
        print("3. Coding News Module")
        print("4. Search AI Tools")
        print("5. Reports")
        print("0. Exit")

        choice = input("\nSelect Option : ")

        if choice == "1":
            os.system("python -m python.modules.github.github_main")

        elif choice == "2":
            os.system("python -m python.modules.ai_tools.ai_tools_main")

        elif choice == "3":
            os.system("python -m python.modules.coding.coding_main")

        elif choice == "4":
            os.system("python -m python.modules.search.search_main")

        elif choice == "5":
            os.system("python -m python.modules.reports.report_main")

        elif choice == "0":
            print("\nGood Bye 👋")
            break

        else:
            print("\nInvalid Choice")


if __name__ == "__main__":
    main()