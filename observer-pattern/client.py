from abc import ABC, abstractmethod
from dataclasses import dataclass
import uuid 
from typing import List, Dict, Any
import datetime


@dataclass(frozen=True)
class Event:
    data: List[Dict[Any, Any]]
    timestamp: int



class Subscriber(ABC):
    """
    I am the interface for subscribers to implement
    """
    def __init__(self):
        self.id = uuid.uuid4()

    @abstractmethod
    def update(self, e: Event) -> None:
        """
        Implement me to confirm updating logic.
        """
        pass


class EchoSubscriber(Subscriber):
    def update(self, e: Event) -> None:
        print(f"{e.data} occured @ {e.timestamp}")


class EventHandler:
    def __init__(self, subscribers: Dict[str, Subscriber]):
        self.subscribers = subscribers

    def subscribe(self, s: Subscriber) -> None:
        if s.id in self.subscribers:
            raise ValueError(f"Can not add subscriber who is already subscribed {s.id}")
        self.subscribers[s.id] = s

    def unsubscribe(self, s_id: int) -> None:
        if s_id not in self.subscribers:
            raise KeyError(f"Can not unsubscribe if not subscribed! {s_id}")
        del self.subscribers[s_id]
        
    def notifyAll(self, event: Event) -> None:
        for subscriber in self.subscribers.values():
            subscriber.update(event)

def get_now_timestamp() -> float:
    now = datetime.datetime.now()
    return datetime.datetime.timestamp(now) * 1000


def client():
    subscribers = {inst.id: inst for inst in [EchoSubscriber() for _ in range(10)]}

    handler = EventHandler(subscribers=subscribers)

    now = get_now_timestamp()
    event = Event(
        data=[{"message": "send this email"}, {"message": "make a log entry"}],
        timestamp=now
        )

    handler.notifyAll(event=event)

client()