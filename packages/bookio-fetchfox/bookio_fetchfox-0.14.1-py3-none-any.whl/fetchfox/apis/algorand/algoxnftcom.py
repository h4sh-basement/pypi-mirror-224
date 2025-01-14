from typing import Iterable, Tuple

from fetchfox import rest
from fetchfox.checks import check_str

BASE_URL = "https://api.algoxnft.com"


def get(service: str, params: dict = None, version: int = 1) -> Tuple[dict, int]:
    return rest.get(
        url=f"{BASE_URL}/v{version}/{service}",
        params=params or {},
    )


def get_listings(creator_address: str) -> Iterable[dict]:
    check_str(creator_address, "algoxnftcom.creator_address")
    creator_address = creator_address.strip().upper()

    response, status_code = get(f"nft-explorer/creator/{creator_address}")

    yield from response
