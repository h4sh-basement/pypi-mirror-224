import re
from datetime import datetime
from typing import Any, Union

from pydantic import BaseModel, BaseConfig

from controller.core.db import DataBase
from controller.core.functions import count


def log(func):
    def wrapper(self, *args, **kwargs):
        self.send_log(func, args, kwargs)
        response = func(self, *args, **kwargs)
        return response

    return wrapper


class Model(BaseModel):
    _db: DataBase
    _func_name: str = None
    _schema: str = 'public'
    _is_core: bool = False  # Указать корневую модель от которой будут наследоваться остальные модели,

    # для автоматического определения func_name TODO: Доработать с использованием наследования

    class Config(BaseConfig):
        use_enum_values = True
        validate_all = True
        validate_assignment = True
        allow_reuse = True
        error_msg_templates = {
            'type_error.none.not_allowed': 'Поле не может быть пустым',
            'value_error.missing': "Поле обязательное",
            'value_error.const': "Заданное значение не входит в список разрешенных для этого поля"
        }

    def __str__(self):
        return f"{self.__class__.__name__}({super(Model, self).__str__()})"

    @property
    def sql_func(self):
        # TODO: Добавить call or select * from
        return f"{self.func_name}({', '.join(self._db.get_query(self.dict()))})"

    @staticmethod
    def camel_to_snake(full_name):
        def to_snake(name):
            return re.sub(r'(?<!^)(?=[A-Z])', '_', name)

        return '.'.join(map(to_snake, full_name.split('.'))).lower()

    @property
    def func_name(self):
        parent = self.__class__
        classes = [parent]
        while getattr(parent.__base__, '_is_core', False) and getattr(parent.__base__.__base__, '_is_core', False):
            parent = parent.__base__
            if getattr(parent.__base__, '_is_core', False):
                classes.append(parent)
        return self._func_name or f'{self._schema}.{self.camel_to_snake(classes[-1].__qualname__)}'

    @staticmethod
    def catch_response(data: Any):
        """Обработка ответа"""
        return data

    def send_log(self, func, args, kwargs):
        now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        print(f'{now}: Вызов {self.sql_func}')


class FunctionModel(Model):

    def __len__(self):
        return self.length()

    @log
    def get(self, limit: int = 1) -> Union[dict, list]:
        """Получение n элементов"""
        with self._db as db:
            return self.catch_response(
                db.function(attrs=self.dict(), func_name=self.func_name, response_limit=limit))

    @log
    def all(self):
        """Получение всех элементов"""
        with self._db as db:
            return self.catch_response(db.function(attrs=self.dict(), func_name=self.func_name, response_limit=-1))

    @log
    def length(self) -> int:
        """Получение количество строк"""
        with self._db as db:
            return db.function(attrs=self.dict(),
                               func_name=self.func_name, response_limit=1,
                               aggregate=count()).get('count', 0)


class ProcedureModel(Model):
    @log
    def execute(self):
        """Выполнить"""
        with self._db as db:
            return self.catch_response(db.procedure(attrs=self.dict(), func_name=self.func_name))
