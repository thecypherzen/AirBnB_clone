"""TestCases for file_storage Module"""

import os
import sys
from unittest import TestCase, main
from uuid import uuid4 as idgen
from datetime import datetime as dt


class TestFileStorage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hbnb_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            )
        )
        if cls.hbnb_dir not in sys.path:
            sys.path.append(cls.hbnb_dir)

        from models import base_model, amenity, city, place,\
            review, state, user
        from models.engine import file_storage

        cls.BM = base_model.BaseModel
        cls.FS = file_storage.FileStorage
        cls.AM = amenity.Amenity
        cls.City = city.City
        cls.Place = place.Place
        cls.Rev = review.Review
        cls.Sta = state.State
        cls.Usr = user.User
        cls.store = cls.FS()
        cls.review = cls.Rev(user_id="xyz-23",
                             text="very cozy and comfy",
                             place_id="KN/LV/0923-3G")

    def test_01_docs_check(self):
        models_pkg = __import__("models")
        engine_pkg = getattr(models_pkg, "engine")
        file_storage = getattr(engine_pkg, "file_storage")

        with self.subTest(msg="1:fs module has no docs"):
            fs_module_docs = file_storage.__doc__.split()
            self.assertTrue(len(fs_module_docs) > 1)
        with self.subTest(msg="2:fs class has no docs"):
            fs_class = getattr(file_storage, "FileStorage")
            fs_class_docs = fs_class.__doc__.split()
            self.assertTrue(len(fs_class_docs) > 1)
        with self.subTest(msg="3:fs.<all>: No docs found"):
            fs_all_docs = getattr(fs_class, "all").__doc__.split()
            self.assertTrue(len(fs_all_docs) > 1)
        with self.subTest(msg="4:fs.<new>: Docs Fail"):
            fs_new_docs = getattr(fs_class, "new").__doc__.split()
            self.assertTrue(len(fs_new_docs) > 1)
        with self.subTest(msg="5:fs.<reload>: Docs Fail"):
            fs_reload_docs = getattr(fs_class, "reload").__doc__.split()
            self.assertTrue(len(fs_reload_docs) > 1)
        with self.subTest(msg="6:fs.<save>: No docs found"):
            fs_save_docs = getattr(fs_class, "save").__doc__.split()
            self.assertTrue(len(fs_save_docs) > 1)

    def test_02_are_hidden(self):
        with self.subTest(msg="1:__filepath Check Fail"):
            with self.assertRaises(AttributeError) as err:
                file_path = getattr(self.FS, "__file_path")
                errmsg = "type object 'FileStorage' has no " + \
                    "attribute '__file_path'"
                self.assertEqual(err, errmsg)
        with self.subTest(msg="2:__objects Check Fail"):
            with self.assertRaises(AttributeError) as err:
                file_path = getattr(self.FS, "__objects")
                errmsg = "type object 'FileStorage' has no " + \
                    "attribute '__objects'"
                self.assertEqual(err, errmsg)

    def test_03_all_mthd_check(self):
        store_dict = self.store.all()
        with self.subTest(msg="1:all_dict check Fail"):
            self.assertIsInstance(store_dict, dict)

    def test_04_new_mthd_check(self):
        user = self.Usr()
        user_key = f"{user.__class__.__name__}.{user.id}"
        user.save()
        self.store.reload()
        store_objs = self.store.all()
        self.assertTrue(user_key in store_objs.keys())

    def test_05_reload_check(self):
        self.review.save()
        self.store.reload()
        new_store_items = self.store.all()
        model_key = f"{self.review.__class__.__name__}.{self.review.id}"
        self.assertIn(model_key, new_store_items)


if __name__ == "__main__":
    main()
