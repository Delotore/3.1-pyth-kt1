from pydantic import BaseModel, field_validator

class Category(BaseModel):
    name: str
    color: str


class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str = "hiden"

    @field_validator("title")
    @classmethod
    def lenght_validity(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError(
                "Название задачи должно содержать минимум 3 символа"
            )
        return value

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool = False
    category: Category
