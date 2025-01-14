from ...client import AuthenticatedClient


def read(id: str, *, client: AuthenticatedClient, image_name: str):
    url = "{}/api/v1/cells/{id}/images/{imageName}/thumbnail".format(
        client.base_url, id=id, imageName=image_name
    )
    response = client.get(url, headers=client.token_headers)
    return response.content
