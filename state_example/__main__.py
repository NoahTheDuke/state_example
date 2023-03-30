from state_example import stateful, pure


def main():
    print("running stateful example twice")
    result1 = stateful.main()
    result2 = stateful.main()
    print(f"Are they equal? {result1 == result2}")

    print("running pure example twice")
    result1 = pure.main()
    result2 = pure.main()
    print(f"Are they equal? {result1 == result2}")


if __name__ == "__main__":
    main()
