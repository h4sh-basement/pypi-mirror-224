from .structures import EventCall, EventHandler, EventSupport, Contains
from .exceptions import UncancellableEvent
from .event_space import EventSpace, global_event_space

__name__ = "pyding"
__version__ = "1.8.2"

def __getattr__(attr):
    return global_event_space.__getattribute__(attr)

def __dir__():
    return global_event_space.__dir__()