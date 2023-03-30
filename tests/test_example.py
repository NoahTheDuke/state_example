import unittest
import state_example.stateful as stateful
import state_example.pure as pure

expected = [
    {"first_name": "Noah", "last_name": "Bogart", "age": 35},
    {"first_name": "Liam", "last_name": "Bogart", "age": 28},
]


class TestCase(unittest.TestCase):
    def test_stateful(self):
        results = stateful.main()
        # this one succeeds
        self.assertEqual(
            results,
            expected,
        )

        results = stateful.main()
        # This one fails
        self.assertNotEqual(
            results,
            expected,
        )

    def test_pure(self):
        results = pure.main()
        # this one succeeds
        self.assertEqual(results, expected)

        results = pure.main()
        # This one suceeds
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()
