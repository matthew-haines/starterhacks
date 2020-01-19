import sys
import database.database as database

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Bad args")
        sys.exit(0)

    db = database.load_data()
    sample = db[-1]
    for _ in range(int(sys.argv[1])):
        db.append(sample)

    database.save_data(db)
    print(f"Saved {sys.argv[1]} versions of the most recent handshake")

