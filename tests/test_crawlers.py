import os
import tempfile
import pytest
import asyncio

from crawlers.page.crawl_page import crawl_page
from crawlers.local.crawl_local import crawl_local
from crawlers.site.crawl_site import crawl_site

# Test case for page crawling using https://docs.crawl4ai.com/
@pytest.mark.asyncio
async def test_page_crawling():
    url = "https://docs.crawl4ai.com/"
    markdown = await crawl_page(url)
    # Check that some markdown content is returned
    assert markdown is not None, "Expected non-None markdown output for a valid URL"
    # Optionally, verify that the content contains a known keyword from the docs
    assert "Crawl4AI" in markdown or "Documentation" in markdown, "Markdown should include expected text"

# Test case for local HTML crawling using a temporary file
@pytest.mark.asyncio
async def test_local_crawling():
    html_content = (
        "<html><head><title>Test Page</title></head>"
        "<body><p>Hello, this is a test.</p></body></html>"
    )
    # Create a temporary directory and write a test HTML file into it
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_file = os.path.join(tmpdirname, "test.html")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        # Run the local crawler on the temporary directory
        results = await crawl_local(tmpdirname)
        # We expect exactly one HTML file processed
        assert len(results) == 1, "Expected one HTML file to be processed"
        file_path, content = results[0]
        assert "Hello, this is a test." in content, "Content from the local file should be read correctly"

# Test case for site crawling. Note: This test assumes that https://docs.crawl4ai.com/ has a sitemap.xml.
# If it does not, your crawl_site function will log an error and return an empty list.
@pytest.mark.asyncio
async def test_site_crawling():
    url = "https://docs.crawl4ai.com/"
    results = await crawl_site(url)
    # Verify that results is a list.
    assert isinstance(results, list), "Expected results to be a list"
    # If no sitemap exists, results may be empty.
    # You can adjust the test based on the expected behavior for missing sitemaps.