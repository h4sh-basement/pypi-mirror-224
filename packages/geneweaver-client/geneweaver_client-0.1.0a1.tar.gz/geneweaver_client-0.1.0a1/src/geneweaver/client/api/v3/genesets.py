"""Function for interacting with the Geneweaver API."""
import requests
from geneweaver.client.core.config import settings


def get_genesets(access_token: str) -> list:
    """Get all visible genesets"""
    return requests.get(
        settings.api_v3_path() + "/genesets",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()


def get_geneset(access_token: str, geneset_id: str):
    """Get a specific geneset"""
    return requests.get(
        settings.api_v3_path() + f"/genesets/{geneset_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()
