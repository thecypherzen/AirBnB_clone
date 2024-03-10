"""BaseModel TestCases"""

import os
import sys
from datetime import datetime as dt, timedelta as td
from uuid import uuid4 as idgen
from unittest import TestCase, main


class TestBaseModel(TestCase):
    @classmethod
    def setUpClass(cls):
        from models import base_model as bm

        cls.hbnb = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            ))
        cls.base = bm.BaseModel()
        cls.base.name = "Jimalaika"
        cls.BM = bm.BaseModel
        if cls.hbnb not in sys.path:
            sys.path.append(cls.hbnb)

    # check module documentation
    def test_01_has_docs(self):
        models_pkg = __import__("models")
        base_module = getattr(models_pkg, "base_model")
        with self.subTest("1:bm docs check"):
            docs = base_module.__doc__.split()
            self.assertTrue(len(docs) > 1)
        with self.subTest(msg="2:BM docs check"):
            base_obj = getattr(base_module, "BaseModel")
            docs = base_obj.__doc__.split()
            self.assertTrue(len(docs) > 1)
        with self.subTest(msg="3:__init__ docs check"):
            base_init = getattr(base_obj, "__init__")
            docs = base_init.__doc__.split()
            self.assertTrue(len(docs) > 1)
        with self.subTest(msg="4:__str__ docs check"):
            base_str = getattr(base_obj, "__str__")
            docs = base_str.__doc__.split()
            self.assertTrue(len(docs) > 1)
        with self.subTest(msg="5:save docs check"):
            base_save = getattr(base_obj, "save")
            docs = base_save.__doc__.split()
            self.assertTrue(len(docs) > 1)
        with self.subTest(msg="6:to_dict docs check"):
            base_td = getattr(base_obj, "to_dict")
            docs = base_td.__doc__.split()
            self.assertTrue(len(docs) > 1)

    def test_02_check_types(self):
        with self.subTest(msg="1:obj is <BaseModel>"):
            self.assertIs(self.base.__class__.__name__, "BaseModel")
        with self.subTest(msg="2:id is not <str>"):
            self.assertIsInstance(self.base.id, str)
        with self.subTest(msg="3:updated_at is not <datetime>"):
            self.assertIsInstance(self.base.updated_at, dt)
        with self.subTest(msg="4:created_at is not <datetime>"):
            self.assertIsInstance(self.base.created_at, dt)

    def test_03_attributes(self):

        id_check = str(idgen())
        date_now = dt.now()
        with self.subTest(msg="1:has id attr"):
            id_val = getattr(self.base, 'id')
            self.assertIsNot(id_val, None)
            with self.subTest(msg="1a:id is str"):
                self.assertIsInstance(id_val, str)
        with self.subTest(msg="2:has created_at attr"):
            created_at = getattr(self.base, 'created_at')
            self.assertIsNot(created_at, None)
            with self.subTest(msg="2a:created_at is datetime"):
                self.assertIsInstance(created_at, type(date_now))
        with self.subTest(msg="3:has updated_at attr"):
            updated_at = getattr(self.base, 'updated_at')
            self.assertIsNot(updated_at, None)
            with self.subTest(msg="3a:updated_at is datetime"):
                self.assertIsInstance(updated_at, type(date_now))

    def test_04_print(self):
        expected = f"[{self.base.__class__.__name__}] ({self.base.id})" + \
            f" {self.base.__dict__}"
        with open(".temp", 'w') as f:
            print(self.base, end="", file=f)
        with open(".temp", 'r') as f:
            received = f.read()
        os.remove(".temp")
        with self.subTest(msg="1:print works well"):
            self.assertEqual(expected, received)

    def test_05_save_updates_time(self):
        updated_at_before = self.base.updated_at
        self.base.save()
        updated_at_after = self.base.updated_at
        diff = updated_at_after - updated_at_before
        diff = diff.total_seconds()
        self.assertTrue(diff > 0)

    def test_06_to_dict_check(self):
        obj_dic = self.base.to_dict()
        with self.subTest(msg="1:obj is dict"):
            self.assertIsInstance(obj_dic, dict)
        with self.subTest(mgs="2:dict has all attrs"):
            with self.subTest(msg=f"2a:__class__ not in dict"):
                keys = list(obj_dic.keys())
                self.assertTrue("__class__" in keys and
                                obj_dic["__class__"] is not None)

            with self.subTest(msg=f"2b:id not <dict>"):
                self.assertIsInstance(obj_dic['id'], str)
            with self.subTest(msg=f"2c:created_at is not <str>"):
                self.assertIsInstance(obj_dic['created_at'], str)
            with self.subTest(msg=f"2d:updated_at is not <str>"):
                self.assertIsInstance(obj_dic['updated_at'], str)
            keys.remove("__class__")
            with self.subTest(msg=f"2d:check keys fail"):
                for key in keys:
                    with self.subTest(msg=f"key:{key} not found"):
                        base_attr = getattr(self.base, key)
                        self.assertFalse(base_attr is None)

    def test_07_new_obj_from_dict(self):
        obj_dict = self.base.to_dict()
        with self.subTest(msg="1:model from dict fail"):
            new_obj = self.BM(**obj_dict)
            with self.subTest(msg="1a:new obj create fail"):
                self.assertIsNotNone(new_obj)
            with self.subTest(msg="1b:new obj type fail"):
                self.assertIs(self.base.__class__.__name__,
                              new_obj.__class__.__name__)
            with self.subTest(msg="1c: new obj is different"):
                self.assertIsNot(self.base, new_obj)

    def test_08_create_obj_with_kwargs(self):
        file_path = ".temp"
        first_obj = self.BM(f_name="Christenson", l_name="Alubarika")
        first_obj_dict = first_obj.to_dict()
        new_obj = self.BM(**first_obj_dict)
        with open(file_path, 'w+') as f:
            print(first_obj, file=f, end='')
            f.seek(0)
            first_res = f.read()
            f.seek(0)
            f.truncate()
            print(new_obj, file=f, end='')
            f.seek(0)
            new_res = f.read()
        self.assertEqual(first_res, new_res)

    def test_09_create_obj_with_non_dicts(self):
        with self.subTest(msg="1:passing None failed"):
            new_obj = self.BM(None)
            self.assertIsNotNone(new_obj)
        with self.subTest(msg="2:passing List failed"):
            new_obj = self.BM(["here", "there", 13])
            self.assertIsNotNone(new_obj)
        with self.subTest(msg="3:passing Tuple failed"):
            new_obj = self.BM((2, 3, 4))
            self.assertIsNotNone(new_obj)


if __name__ == "__main__":
    main()
