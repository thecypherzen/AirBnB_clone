"""TestCases for file_storage Module"""

import os
import sys
from unittest import TestCase, main
from uuid import uuid4 as idgen
from datetime import datetime as dt


class CheckerClass():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
        self.id = str(idgen())
        self.created_at = dt.now()
        self.updated_at = self.created_at

    def to_dict(self):
        from copy import deepcopy
        # update timestamp values
        obj_copy = deepcopy(self)
        obj_copy.created_at = obj_copy.created_at.isoformat()
        obj_copy.updated_at = obj_copy.updated_at.isoformat()

        # get dictionary
        temp = obj_copy.__dict__
        temp['__class__'] = self.__class__.__name__
        return temp


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

        from models import base_model
        from models.engine import file_storage

        cls.BM = base_model.BaseModel
        cls.FS = file_storage.FileStorage
        cls.store = cls.FS()
        cls.model = CheckerClass(gender="Male", cohort="19")

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
        store = self.FS()
        store_dict = store.all()
        with self.subTest(msg="1:all_dict check Fail"):
            self.assertIsInstance(store_dict, dict)

    def test_03_new_mthd_check(self):
        model_key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.store.new(self.model)
        store_objs = self.store.all()
        self.assertTrue(model_key in store_objs)

    def test_04_save_mthd_check(self):
        self.store.save()
        save_store = self.FS()
        save_store_items = save_store.all()
        model_key = f"{self.model.__class__.__name__}.{self.model.id}"
        with self.subTest(msg="1:Reload Fail"):
            self.assertIn(model_key, save_store_items)

    def test_05_reload_check(self):
        new_store = self.FS()
        new_store.reload()
        new_store_items = new_store.all()
        model_key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(model_key, new_store_items)


if __name__ == "__main__":
    main()
