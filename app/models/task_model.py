from typing import List, Dict, Any
from datetime import datetime
class Task:
    def __init__(self, 
                 tenantName: str, 
                 reference: str, 
                 documentCreator: str, 
                 dateCreated: datetime, 
                 info: str, 
                 tags: List[str], 
                 downloadKey: str, 
                 fields: Dict[str, any]
                 ):
        self.tenantName = tenantName
        self.reference = reference
        self.documentCreator = documentCreator
        self.dateCreated = dateCreated
        self.info = info
        self.tags = tags
        self.downloadKey = downloadKey
        self.fields = fields
    def to_dict(self) -> Dict[str, Any]:
        return {
            "tenantName": self.tenantName,
            "reference": self.reference,
            "documentCreator": self.documentCreator,
            "dateCreated": self.dateCreated.isoformat() if isinstance(self.dateCreated, datetime) else self.dateCreated,
            "info": self.info,
            "tags": self.tags,
            "downloadKey": self.downloadKey,
            "fields": self.fields,
        }
    # def save_task(self) -> Dict[str, Any]:
        
        
        


    