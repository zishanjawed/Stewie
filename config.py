# config.py
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="RAG Application Crawler")
    parser.add_argument(
        "--mode", type=str, choices=["site", "page", "local"], default="page",
        help="Crawling mode: 'site' for full site, 'page' for single page, 'local' for local HTML files"
    )
    parser.add_argument("--url", type=str, help="URL to crawl (for site or page mode)")
    parser.add_argument("--dir", type=str, help="Directory path for local HTML crawling")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()