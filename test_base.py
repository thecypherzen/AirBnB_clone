from models import base_model

BaseModel = base_model.BaseModel

bm = BaseModel()
bm.name = "George Hikkins"
bm.email = "credit.alert@jburg.xyz"
bm.countr = "Estonia"
bm.save()
print("test_base.py\n   > ",bm)
