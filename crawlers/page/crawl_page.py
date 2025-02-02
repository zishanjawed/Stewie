import asyncio
import logging
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

logger = logging.getLogger(__name__)

async def crawl_page(url: str):
    logger.info(f"Starting crawl for single page: {url}")
    browser_config = BrowserConfig(headless=True, verbose=True)
    
    # Create a basic run configuration using CacheMode.BYPASS and the default markdown generator.
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=DefaultMarkdownGenerator()  # Instantiate the generator
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)
        if result.success:
            logger.info(f"Successfully crawled {url}")
            return result.markdown  # Return the markdown content
        else:
            logger.error(f"Failed to crawl {url}: {result.error_message}")
            return None