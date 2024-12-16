from postgres import perform_postgres_action
# from mongo import perform_mongo_action

def main():
    print("Testing PostgreSQL...")
    perform_postgres_action()

    print("Testing MongoDB...")
    # perform_mongo_action()

    

if __name__ == "__main__":
    main()
