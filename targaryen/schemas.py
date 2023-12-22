from ninja import Schema, ModelSchema
from targaryen.models import Person


class DragonOut(Schema):
    name: str
    birth_year: int


class PersonOut(ModelSchema):
    full_name: str

    class Config:
        model = Person
        model_fields = ["id", "birth_year"]

    @staticmethod
    def resolve_full_name(obj) -> str:
        return f"{obj.name}, {obj.title}"
