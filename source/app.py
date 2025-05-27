import logging
from contextlib import asynccontextmanager

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from source.classes import ModelInput, ModelOutput
from source.inference import load_model, predict

model = None
logger = logging.getLogger('uvicorn.info')


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Функция для загрузки модели и токенайзера
    """
    global model
    model = load_model(path='models/model.pkl')
    logger.info('Model loaded')
    yield
    del model


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def return_info() -> RedirectResponse:
    """
    Корневой эндпоинт, перенаправляющий на /docs
    :return:
    """
    return RedirectResponse(url='/docs')


@app.post('/pred')
async def pred(data: ModelInput):
    """
    Эндпоинт для получения предсказания модели.
    Принимает post запрос с json файлом с указанным в example форматом.
    Пример удачного ответа можно увидеть в Responses: 200
    """
    df = pd.DataFrame([data.model_dump()])
    prediction = predict(model=model, df=df)
    return ModelOutput(label=prediction[0])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=30)
