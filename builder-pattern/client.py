from typing import Any, Self


# TODO implement Query builder pattern for mongodb
class QueryBuilder:
    def __init__(self):
        self._select = []
        self._where = []
        self._from = []
        self._sort = []
        self._groupby = []
        self._query = []

    def build(self) -> str:
        # TODO this will create the final query string
        select = f"SELECT {' '.join(s for s in self._select)} "
        _from = f"FROM {' '.join(s for s in self._from)}"
        where = f"WHERE {' '.join(s for s in self._where)}"
        return select + _from + where

    def select(self, statement: str) -> Self:
        self._select += [statement]
        return self

    def where(self, statement: str) -> Self:
        self._where += [statement]
        return self


query = QueryBuilder().select("field as Field").build()
print(query)
