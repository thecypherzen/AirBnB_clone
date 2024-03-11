"""Amenities TestCases"""

import os
import sys
from unittest import TestCase, main


class TestAmenity(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hbnb_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )

        if cls.hbnb_dir not in sys.path:
            sys.path.append(cls.hbnb_dir)

        from models import base_model, amenity
        from models.engine import file_storage

        cls.BM = base_model.BaseModel
        cls.AM = amenity.Amenity
        cls.FS = file_storage.FileStorage
        cls.amenity = cls.AM(name="JukeBox")

    def test_10_amenity_init(self):
        pass


if __name__ == "__main__":
    main()
