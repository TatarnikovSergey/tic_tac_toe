# gameparts/exceptions.py

class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за пределами игрового поля'


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
