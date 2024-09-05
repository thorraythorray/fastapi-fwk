from tortoise import fields, Model
from pydantic import BaseModel, Field


class PaginationSchema(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1)


class BaseTimestampModel(Model):
    create_tm = fields.DatetimeField(auto_now_add=True)
    update_tm = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True