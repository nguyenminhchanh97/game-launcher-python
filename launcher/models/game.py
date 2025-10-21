from pydantic import BaseModel, Field
from typing import List

class Game(BaseModel):
    id: str
    name: str
    platform: str = "windows"
    tags: List[str] = Field(default_factory=list)
    exe_path: str = ""
    work_dir: str = ""
    args: str = ""
