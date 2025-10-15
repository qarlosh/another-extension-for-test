from connect_ext.events import AnotherExtensionForTestEventsApplication


def test_handle_asset_purchase_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {"id": 1}
    ext = AnotherExtensionForTestEventsApplication(
        connect_client, logger, config,
    )
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == "success"
