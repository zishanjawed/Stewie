import asyncio
import os
import logging

logger = logging.getLogger(__name__)

async def process_local_html_file(file_path: str):
    logger.info(f"Processing local file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Here, you could further process the HTML (chunking, extraction, etc.)
        return content
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        return None

async def crawl_local(directory: str):
    logger.info(f"Starting local crawl in directory: {directory}")
    results = []
    # Walk the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):
                file_path = os.path.join(root, file)
                content = await process_local_html_file(file_path)
                results.append((file_path, content))
    logger.info(f"Processed {len(results)} HTML files from {directory}")
    return results