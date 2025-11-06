from typing import List

from pydantic import BaseModel


class CreateLecturerRequestDTO(BaseModel):
    name: str
    id: int
    courses: List[str]
    