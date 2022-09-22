from abc import ABC, abstractmethod
from typing import List, Dict


class SparkRunner:
    def __init__(self, url: str, port: int) -> None:
        self.url = url
        self.port = port

    def run(self, query: str) -> List[Dict]:
        print(f"Running query: {query} \non {self.url}:{self.port} cluster...")
        return [{"id": 1, "name": "some name", "alive": True}, {"id": 2, "name": "some other", "alive": False}]

    
class ResourceFacade(ABC):
    """
    Facade for accessing resources.
    """
    @abstractmethod
    def get(self) -> List[Dict]:
        """
        Implement access to resource
        """

class MonthlyTurbineAvailibilityFacade(ResourceFacade):
    """
    I return monthly turbine availibility.
    """
    def __init__(self, db: SparkRunner, table_name: str) -> None:
        self.db = db
        self.table_name = table_name

    def get(self, ids: List[int], day: str) -> List[Dict]:
        query = f"""
        SELECT * FROM {self.table_name}
        WHERE date = {day} AND id IN {tuple(ids)} 
        """
        return self.db.run(query)

def client(facade: ResourceFacade) -> None:
    """
    Client code operates on facade of type ResourceFacade
    """
    # details parsed from event
    ids, date = [1, 2], "2022-09-12"

    # result is obtained from abstract facade instance
    result = facade.get(ids=ids, day=date)
    print(result)


db_cluster = SparkRunner("internal", 65685)
facade = MonthlyTurbineAvailibilityFacade(db_cluster, "availibilities")

client(facade)