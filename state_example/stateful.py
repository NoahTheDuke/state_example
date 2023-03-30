import itertools as it

global_state = []


class Database:
    def query(self, keys):
        return list(
            it.chain.from_iterable(
                filter(lambda row: row.get("first_name") == key, global_state)
                for key in keys
            )
        )

    def update(self, val):
        global_state.append(val)


db = Database()


def do_stuff():
    db.update(
        {"first_name": "Noah", "last_name": "Bogart", "age": 35},
    )
    db.update(
        {"first_name": "Liam", "last_name": "Bogart", "age": 28},
    )

    return db.query(["Noah", "Liam"])


def main():
    rows = do_stuff()
    return rows


if __name__ == "__main__":
    rows = main()
    print([row["first_name"] for row in rows])
