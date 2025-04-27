import pytest
from app.threshold import split_secret, recover_secret

@pytest.mark.asyncio
async def test_split_and_recover_exact_threshold():
    secret = "a"
    data = await split_secret(secret=secret, shares=5, threshold=3)
    shares = data["shares"]
    prime = data["prime"]

    result = await recover_secret(parts=shares[:3], prime=prime)
    assert result["secret"] == secret

@pytest.mark.asyncio
async def test_recover_insufficient_shares_raises():
    secret = "b"
    data = await split_secret(secret=secret, shares=5, threshold=4)
    shares = data["shares"]
    prime = data["prime"]

    # при недостаточном числе частей секрет не восстанавливается
    result = await recover_secret(parts=shares[:3], prime=prime)
    assert result["secret"] != secret
