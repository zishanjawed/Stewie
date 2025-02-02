import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from config import parse_args
from utils.logging_config import setup_logging
from crawlers.page.crawl_page import crawl_page
from crawlers.site.crawl_site import crawl_site

from crawlers.local.crawl_local import crawl_local

app = FastAPI()
logger = logging.getLogger(__name__)

class CrawlRequest(BaseModel):
    mode: str  # "site", "page", or "local"
    url: str = None
    directory: str = None

@app.post("/crawl")
async def crawl(request: CrawlRequest):
    mode = request.mode.lower()
    if mode == "page":
        if not request.url:
            raise HTTPException(status_code=400, detail="URL is required for page crawling")
        result = await crawl_page(request.url)
        if result is None:
            raise HTTPException(status_code=500, detail="Page crawling failed")
        return {"markdown": result}
    elif mode == "site":
        if not request.url:
            raise HTTPException(status_code=400, detail="URL is required for site crawling")
        results = await crawl_site(request.url)
        return {"results": [{"url": u, "markdown": md} for u, md in results]}
    elif mode == "local":
        if not request.directory:
            raise HTTPException(status_code=400, detail="Directory path is required for local crawling")
        results = await crawl_local(request.directory)
        return {"results": [{"file": f, "content": content} for f, content in results]}
    else:
        raise HTTPException(status_code=400, detail="Invalid mode")

if __name__ == "__main__":
    args = parse_args()
    setup_logging(verbose=args.verbose)
    uvicorn.run(app, host="0.0.0.0", port=9000)


