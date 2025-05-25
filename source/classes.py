from pydantic import BaseModel, Field
from typing import Literal


class ModelInput(BaseModel):
    age: int = Field(..., description="Возраст пациента", ge=1, le=120)
    sex: Literal[0, 1] = Field(..., description="Пол (1 = мужской, 0 = женский)")
    cp: Literal[0, 1, 2, 3] = Field(..., description="Тип боли в груди (0-3)")
    trestbps: int = Field(..., description="Артериальное давление в покое (мм рт.ст.)", ge=80, le=250)
    chol: int = Field(..., description="Уровень холестерина (мг/дл)", ge=100, le=600)
    fbs: Literal[0, 1] = Field(..., description="Сахар в крови натощак > 120 мг/дл (1 = да, 0 = нет)")
    restecg: Literal[0, 1, 2] = Field(..., description="Результаты ЭКГ в покое (0-2)")
    thalach: int = Field(..., description="Максимальная частота сердечных сокращений", ge=60, le=220)
    exang: Literal[0, 1] = Field(..., description="Стенокардия, вызванная физ. нагрузкой (1 = да, 0 = нет)")
    oldpeak: float = Field(..., description="Депрессия ST, вызванная нагрузкой", ge=0.0, le=10.0)
    slope: Literal[0, 1, 2] = Field(..., description="Наклон пикового сегмента ST (0-2)")
    ca: Literal[0, 1, 2, 3, 4] = Field(..., description="Количество основных сосудов (0-4)")
    thal: Literal[0, 1, 2, 3] = Field(..., description="Талассемия (0-3)")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 52,
                "sex": 1,
                "cp": 0,
                "trestbps": 125,
                "chol": 212,
                "fbs": 0,
                "restecg": 1,
                "thalach": 168,
                "exang": 0,
                "oldpeak": 1.0,
                "slope": 2,
                "ca": 2,
                "thal": 3
            }
        }


class ModelOutput(BaseModel):
    label: int = Field(..., description="Метка модели")
