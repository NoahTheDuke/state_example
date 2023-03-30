import itertools as it


class Database:
    def __init__(self):
        self.state = []

    def query(self, keys):
        return list(
            it.chain.from_iterable(
                filter(lambda row: row.get("first_name") == key, self.state)
                for key in keys
            )
        )

    def update(self, val):
        self.state.append(val)


def do_stuff(db, rows):
    for val in rows:
        db.update(val)

    return db.query(["Noah", "Liam"])


def main():
    db = Database()
    rows = [
        {"first_name": "Noah", "last_name": "Bogart", "age": 35},
        {"first_name": "Liam", "last_name": "Bogart", "age": 28},
    ]
    rows = do_stuff(db, rows)
    return rows


if __name__ == "__main__":
    rows = main()
    print([row["first_name"] for row in rows])
