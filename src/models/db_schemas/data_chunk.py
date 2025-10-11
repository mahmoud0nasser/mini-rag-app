from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    id: Optional[ObjectId] =Field(None, alias="_id")  # MongoDB document ID
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    chunk_asset_id: ObjectId  # Reference to Asset if applicable

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
        
        return [
            {
                "key": [
                    ("chunk_project_id", 1) # 1 for ascending index & -1 for descending index
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ] 