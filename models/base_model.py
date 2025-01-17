from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(hash(datetime.now()))
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

class SimpleStorage:
    def serialize(self, obj):
        return "|".join(f"{k}={v}" for k, v in vars(obj).items())
    
    def deserialize(self, data, cls):
        obj = cls()
        pairs = data.split("|")
        for pair in pairs:
            key, value = pair.split("=")
            setattr(obj, key, value)
        return obj