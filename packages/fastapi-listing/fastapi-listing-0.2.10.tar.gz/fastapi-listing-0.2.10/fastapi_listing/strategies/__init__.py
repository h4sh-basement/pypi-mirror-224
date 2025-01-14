from fastapi_listing.strategies.query_strategy import QueryStrategy
from fastapi_listing.paginator import PaginationStrategy   # noqa: F401
from fastapi_listing.sorter import SortingOrderStrategy   # noqa: F401


class ModuleInterface:
    """
    Represents a strategy interface. A strategy should have a constant NAME
    This module must be registered by strategy factory
    strategy_factory.register(NAME, StrategyClass)

    Once we are done with this we can directly import the module
    and inject it with our listing via module.NAME
    """
    NAME: str = "abc_strategy"
