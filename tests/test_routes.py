import unittest
from web_app import create_app
from datetime import datetime
from db.models import Base


class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app(database_url="sqlite:///:memory:")  # in-memory database
        self.client = self.app.test_client()

        # set up database schema
        with self.app.app_context():
            engine = self.app.session_local.kw["bind"]
            Base.metadata.create_all(engine)

    def tearDown(self):
        pass  # no cleanup neaded, in-memory db disappears

    def test_submit_workout_and_get_last_exercise_data(self):
        """
        Unit test to check the flask route saves to the db and
        check the flask route to get the last instance of a certain exercise.
        """
        payload = {
            "date": datetime.today().strftime("%Y-%m-%d"),
            "notes": "Unit test workout",
            "exercises": [
                {
                    "name": "Joe",
                    "sets": [
                        {"reps": 5, "load": 69, "rpe": 8},
                        {"reps": 10, "load": 42}
                    ]
                }
            ]
        }

        # submit workout
        # send POST request
        response = self.client.post(
            "/save_workout",
            json=payload
        )

        # check response
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "success")

        # get last exercise data
        # send GET request
        response = self.client.get(
                "/get_last_exercise_data/Joe"
        )

        # check response
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["last_date"],
                         datetime.today().strftime("%Y-%m-%d"))


if __name__ == "__main__":
    unittest.main()
