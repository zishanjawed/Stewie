import asyncio
import logging
import requests
from xml.etree import ElementTree
from crawlers.page.crawl_page import crawl_page

logger = logging.getLogger(__name__)

def fetch_sitemap_urls(sitemap_url: str):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        root = ElementTree.fromstring(response.content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        return urls
    except Exception as e:
        logger.error(f"Error fetching sitemap: {e}")
        return []

async def crawl_site(url: str):
    # Construct the sitemap URL (assumes sitemap.xml is available)
    sitemap_url = url.rstrip("/") + "/sitemap.xml"
    logger.info(f"Fetching sitemap from {sitemap_url}")
    urls = fetch_sitemap_urls(sitemap_url)
    if not urls:
        logger.error("No URLs found in sitemap, aborting site crawl.")
        return []
    
    logger.info(f"Found {len(urls)} URLs in sitemap.")
    results = []
    
    # Limit concurrency to avoid overloading resources
    semaphore = asyncio.Semaphore(5)
    
    async def crawl_with_semaphore(u):
        async with semaphore:
            md = await crawl_page(u)
            return (u, md)
    
    tasks = [crawl_with_semaphore(u) for u in urls]
    results = await asyncio.gather(*tasks)
    return results