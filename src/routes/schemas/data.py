from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str = None
    chunk_size: Optional[int] = 100  # Default chunk size
    overlap_size: Optional[int] = 20      # Default overlap size
    do_reset: Optional[int] = 0  # Default is not to reset

