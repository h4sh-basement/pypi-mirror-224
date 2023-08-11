from typing import Any, Union

from hooks.backend import HooksBackend

try:
    # Extend pickle to support lambdas
    import dill as pickle
    import redis

    class RedisHooksBackend(HooksBackend):
        redis_client = None

        @classmethod
        def initialize(cls, host: str, port: int, **kwargs: Any) -> None:
            cls.redis_client = redis.Redis(host=host, port=port, **kwargs)

        @classmethod
        def load(cls, identifier: str) -> Any:
            if cls.redis_client:
                return pickle.loads(cls.redis_client.get(identifier))
            else:
                raise Exception("Redis client not initialized")

        @classmethod
        def save(cls, identifier: str, value: Any) -> Union[bool, None, Any]:
            if cls.redis_client:
                return cls.redis_client.set(identifier, pickle.dumps(value))
            else:
                raise Exception("Redis client not initialized")

        @classmethod
        def exists(cls, identifier: str) -> bool:
            if cls.redis_client:
                return cls.redis_client.exists(identifier) == 1
            else:
                raise Exception("Redis client not initialized")

        @classmethod
        def reset_backend(cls):
            if cls.redis_client:
                for key in cls.redis_client.scan_iter("*"):
                    cls.redis_client.delete(key)

except ImportError:
    raise ImportError("Redis backend requires redis to be installed")
