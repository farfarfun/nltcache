from typing import Callable

from cachebox import FIFOCache, LFUCache, LRUCache, RRCache, TTLCache, VTTLCache, cached

__all__ = [
    "cache",
    "lru_cache",
    "ttl_cache",
    "vttl_cache",
    "lfu_cache",
    "fifo_cache",
    "rr_cache",
]


def cache(func: Callable, /) -> Callable:
    """Simple LRU cache decorator with a default maxsize of 1000."""
    return cached(LRUCache(maxsize=1000))(func)


def vttl_cache(maxsize: int = 1000, ttl: int = 60) -> Callable:
    """VTTLCache: removes expired elements lazily when accessed.

    VTTLCache: 在访问时才惰性移除已过期的缓存元素。
    """
    return lambda func: cached(VTTLCache(maxsize=maxsize, ttl=ttl))(func)


def ttl_cache(maxsize: int = 1000, ttl: int = 60) -> Callable:
    """TTLCache: automatically removes expired elements.

    TTLCache：自动移除已过期的缓存元素。
    """
    return lambda func: cached(TTLCache(maxsize=maxsize, ttl=ttl))(func)


def lru_cache(maxsize: int = 1000) -> Callable:
    """LRUCache: removes the least recently used element.

    LRUCache：移除缓存中自上次访问以来时间最长的元素。
    """
    return lambda func: cached(LRUCache(maxsize=maxsize))(func)


def lfu_cache(maxsize: int = 1000) -> Callable:
    """LFUCache: removes the least frequently used element.

    LFUCache：移除缓存中访问次数最少的元素，不论其访问时间。
    """
    return lambda func: cached(LFUCache(maxsize=maxsize))(func)


def fifo_cache(maxsize: int = 1000) -> Callable:
    """FIFOCache: removes the oldest element.

    FIFOCache：移除在缓存中停留时间最长的元素。
    """
    return lambda func: cached(FIFOCache(maxsize=maxsize))(func)


def rr_cache(maxsize: int = 1000) -> Callable:
    """RRCache: randomly removes an element when space is needed.

    RRCache: 在必要时随机选择一个元素进行移除，以腾出空间。
    """
    return lambda func: cached(RRCache(maxsize=maxsize))(func)
