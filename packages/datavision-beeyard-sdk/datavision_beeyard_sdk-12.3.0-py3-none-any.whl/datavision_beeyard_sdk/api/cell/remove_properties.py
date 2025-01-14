from ...client import AuthenticatedClient


def delete(id: str, *, client: AuthenticatedClient, keys: [str]):
    url = "{}/api/v1/cells/{id}/properties?keys=".format(client.base_url, id=id)
    for k in keys:
        url = url + k + "&keys="
    response = client.delete(url[:-6], headers=client.token_headers)
    return response
