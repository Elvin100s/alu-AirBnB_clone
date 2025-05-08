"""Core model class with UUID and timestamp management"""
import uuid
from datetime import datetime, timezone

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize with UTC timestamps or reconstruct from dict"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'
                    ).replace(tzinfo=timezone.utc)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now(timezone.utc)
            self.created_at = now
            self.updated_at = now

    def save(self):
        """Update timestamp and trigger storage save"""
        self.updated_at = datetime.now(timezone.utc)
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dict with ISO-format datetime strings"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        for attr in ['created_at', 'updated_at']:
            if attr in new_dict:
                new_dict[attr] = new_dict[attr].isoformat()
        return new_dict

    def __str__(self):
        """Human-readable string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
