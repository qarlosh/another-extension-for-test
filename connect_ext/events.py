from connect.eaas.core.decorators import (
    event,
    variables,
)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
)


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
