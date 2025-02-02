

#	Project Overview:
Describe the purpose of the RAG application and the crawling features (page, site, local) that have been implemented. Mention the use of Crawl4AI, FastAPI, and asynchronous processing.
	•	Project Structure:
Provide a brief directory tree similar to:

.
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── crawlers
│   ├── local
│   │   └── crawl_local.py
│   ├── page
│   │   └── crawl_page.py
│   └── site
│       └── crawl_site.py
└── utils
    └── logging_config.py


	•	Setup and Installation:
Explain how to install dependencies (e.g., pip install -r requirements.txt) and how to set the PYTHONPATH if needed. Include instructions for setting up Playwright:

python -m playwright install chromium


	•	Running the Application:
Describe how to start the FastAPI server:

python main.py --mode page --url "https://docs.crawl4ai.com/" --verbose

Also include how to use curl or Postman to send requests to the /crawl endpoint.

	•	Testing:
Outline how to run unit tests using pytest:

pytest tests/




2. Docker 

docker run -p 8000:8000 lcl-stewie


	3.	Test the Endpoint:
Use curl or Postman to send a POST request to http://localhost:8000/crawl as before.

