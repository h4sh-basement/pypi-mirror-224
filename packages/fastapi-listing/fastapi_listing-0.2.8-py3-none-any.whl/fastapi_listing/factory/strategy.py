

class StrategyObjectFactory:
    def __init__(self):
        self._strategy = {}

    def register_strategy(self, key: str, builder: type):
        if key is None or not key:
            raise ValueError("Invalid type key!")
        if key in self._strategy:
            raise ValueError(f"strategy name: {key}, already in use with {self._strategy[key].__name__}!")
        if not isinstance(builder, object):
            raise ValueError("builder is not a valid callable!")
        self._strategy[key] = builder

    def create(self, key: str, *args, **kwargs) -> object:
        strategy_ = self._strategy.get(key)
        if not strategy_:
            raise ValueError(key)
        return strategy_(*args, **kwargs)

    def aware_of(self, key: str) -> bool:
        return key in self._strategy


strategy_factory = StrategyObjectFactory()
