from mongo import perform_mongo_action
from postgres import perform_postgres_action

def main():
    print("Testing MongoDB...")
    perform_mongo_action()

    print("Testing PostgreSQL...")
    perform_postgres_action()

if __name__ == "__main__":
    main()
