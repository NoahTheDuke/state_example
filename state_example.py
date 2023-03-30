from state_example import stateful, pure


def main():
    print("running stateful example twice")
    stateful.main()
    stateful.main()

    print("running pure example twice")
    pure.main()
    pure.main()


if __name__ == "__main__":
    main()
