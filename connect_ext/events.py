import sys
from functools import reduce
from connect.eaas.core.decorators import (
    event,
    schedulable,
    variables,
)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
    ScheduledExecutionResponse,
)

list_of_bytearrays = []


@variables([
    {
        'name': 'ALLOC_MEM_SIZE_MB',
        'initial_value': '100',
        'secure': False,
    },
])
class AnotherExtensionForTestEventsApplication(EventsApplicationBase):
    @event(
        'asset_purchase_request_processing',
        statuses=['pending', 'approved', 'scheduled'],
    )
    def handle_asset_purchase_request_processing(self, request):
        self.logger.info(
            f"Handle 'asset_purchase_request_processing', request with id {request['id']}"
        )
        return BackgroundResponse.done()

    @schedulable('alloc_mem', '')
    def alloc_mem(self, schedule):
        print(schedule)
        self.logger.info("EXECUTING SCHEDULABLE alloc_mem")
        ba = bytearray(int(self.config['ALLOC_MEM_SIZE_MB']) * 1024 * 1024)
        list_of_bytearrays.append(ba)
        self.logger.info(f"allocated {sys.getsizeof(ba) / 1024 / 1024} MB")
        self.logger.info(f"(total allocated: {reduce(lambda acum, ba: acum + sys.getsizeof(ba), list_of_bytearrays, 0) / 1024 / 1024} MB) ")
        return ScheduledExecutionResponse.done()

    @schedulable('clear_mem', '')
    def clear_mem(self, schedule):
        self.logger.info("EXECUTING SCHEDULABLE clear_mem")
        list_of_bytearrays.clear()
        self.logger.info(f"(total allocated: {reduce(lambda acum, ba: acum + sys.getsizeof(ba), list_of_bytearrays, 0) / 1024 / 1024} MB) ")
        return ScheduledExecutionResponse.done()
