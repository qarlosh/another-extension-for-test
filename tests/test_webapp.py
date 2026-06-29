from connect.eaas.core.testing.testclient import WebAppTestClient

from connect_ext.webapp import AnotherExtensionForTestWebApplication


def test_environment_info():
    client = WebAppTestClient(AnotherExtensionForTestWebApplication)
    response = client.get('/api/environment_info')
    assert response.status_code == 200
    data = response.json()
    assert 'python_version' in data
    assert 'environment' in data
    assert 'packages' in data
