import sys
from pydantic import BaseModel
from functools import reduce

list_of_bytearrays = []


class AllocMemRequest(BaseModel):
    size_mb: int

class AllocMemResponse(BaseModel):
    allocated_mb: int
    total_allocated_mb: int

class ClearMemResponse(BaseModel):
    total_allocated_mb: int


def alloc_mem(logger, request: AllocMemRequest):
    logger.info("EXECUTING SCHEDULABLE alloc_mem")
    ba = bytearray(request.size_mb * 1024 * 1024)
    list_of_bytearrays.append(ba)
    logger.info(f"allocated {sys.getsizeof(ba) / 1024 / 1024} MB")
    logger.info(f"(total allocated: {_get_total_allocated_mb()} MB) ")
    return AllocMemResponse(
        allocated_mb=sys.getsizeof(ba) / 1024 / 1024,
        total_allocated_mb=_get_total_allocated_mb(),
    )


def clear_mem(logger):
    logger.info("EXECUTING SCHEDULABLE clear_mem")
    list_of_bytearrays.clear()
    logger.info(f"(total allocated: {_get_total_allocated_mb()} MB) ")
    return ClearMemResponse(
        total_allocated_mb=_get_total_allocated_mb(),
    )


def _get_total_allocated_mb():
    return reduce(lambda acum, ba: acum + sys.getsizeof(ba), list_of_bytearrays, 0) / 1024 / 1024
