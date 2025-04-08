import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from biofetcher.downloader import sync_download, async_download

def test_sync_download():
    url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    filename = "sync_test.txt"
    sync_download(url, filename)
    assert os.path.exists(filename)
    os.remove(filename)

@pytest.mark.asyncio
async def test_async_download():
    url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    filename = "async_test.txt"
    await async_download(url, filename)
    assert os.path.exists(filename)
    os.remove(filename)
