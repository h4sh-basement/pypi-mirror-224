import re
import requests
from typing import List, Optional, Dict
from dataclasses import dataclass, field

def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

def to_camel_case(data: dict) -> dict:
    return {snake_to_camel(k): v for k, v in data.items() if v is not None}

def camel_to_snake(camel_str: str) -> str:
    snake_str = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_str)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake_str).lower()

def to_snake_case(data: dict) -> dict:
    return {camel_to_snake(k): v for k, v in data.items()}

SEARCH_OPTIONS_TYPES = {
    'query': str,
    'num_results': int,
    'include_domains': list,
    'exclude_domains': list,
    'start_crawl_date': str,
    'end_crawl_date': str,
    'start_published_date': str,
    'end_published_date': str,
    'use_autoprompt': bool,
    'type': str
}

FIND_SIMILAR_OPTIONS_TYPES = {
    'url': str,
    'num_results': int,
    'include_domains': list,
    'exclude_domains': list,
    'start_crawl_date': str,
    'end_crawl_date': str,
    'start_published_date': str,
    'end_published_date': str,
}

def validate_search_options(options: Dict[str, Optional[object]]) -> None:
    for key, value in options.items():
        if key not in SEARCH_OPTIONS_TYPES:
            raise ValueError(f"Invalid option: '{key}'")
        if not isinstance(value, SEARCH_OPTIONS_TYPES[key]):
            raise ValueError(f"Invalid type for option '{key}': Expected {SEARCH_OPTIONS_TYPES[key]}, got {type(value)}")
        if key in ['include_domains', 'exclude_domains'] and not value:
            raise ValueError(f"Invalid value for option '{key}': cannot be an empty list")

def validate_find_similar_options(options: Dict[str, Optional[object]]) -> None:
    for key, value in options.items():
        if key not in FIND_SIMILAR_OPTIONS_TYPES:
            raise ValueError(f"Invalid option: '{key}'")
        if not isinstance(value, FIND_SIMILAR_OPTIONS_TYPES[key]):
            raise ValueError(f"Invalid type for option '{key}': Expected {FIND_SIMILAR_OPTIONS_TYPES[key]}, got {type(value)}")
        if key in ['include_domains', 'exclude_domains'] and not value:
            raise ValueError(f"Invalid value for option '{key}': cannot be an empty list")

@dataclass
class Result:
    title: str
    url: str
    id: str
    score: Optional[float] = None
    published_date: Optional[str] = None
    author: Optional[str] = None
    extract: Optional[str] = None

    def __init__(self, title, url, id, score=None, published_date=None, author=None, **kwargs):
        self.title = title
        self.url = url
        self.score = score
        self.id = id
        self.published_date = published_date
        self.author = author
    def __str__(self):
        return (f"Title: {self.title}\n"
                f"URL: {self.url}\n"
                f"ID: {self.id}\n"
                f"Score: {self.score}\n"
                f"Published Date: {self.published_date}\n"
                f"Author: {self.author}\n"
                f"Extract: {self.extract}")

@dataclass
class DocumentContent:
    id: str
    url: str
    title: str
    extract: str

    def __init__(self, id, url, title, extract, **kwargs):
        self.id = id
        self.url = url
        self.title = title
        self.extract = extract

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"URL: {self.url}\n"
                f"Title: {self.title}\n"
                f"Extract: {self.extract}")

@dataclass
class GetContentsResponse:
    contents: List[DocumentContent]

    def __str__(self):
        return "\n\n".join(str(content) for content in self.contents)

@dataclass
class SearchResponse:
    results: List[Result]
    api: Optional['Metaphor'] = field(default=None, init=False)

    def get_contents(self):
        if self.api is None:
            raise Exception("API client is not set. This method should be called on a SearchResponse returned by the 'search' method of 'Metaphor'.")
        ids = [result.id for result in self.results]
        return self.api.get_contents(ids)

    def __str__(self):
        return "\n\n".join(str(result) for result in self.results)

class Metaphor:
    def __init__(self, api_key: str):
        self.base_url = "https://api.metaphor.systems"
        self.headers = {"x-api-key": api_key, "User-Agent": "metaphor-python 0.1.12"}

    def search(self, query: str, num_results: Optional[int] = None, include_domains: Optional[List[str]] = None,
               exclude_domains: Optional[List[str]] = None, start_crawl_date: Optional[str] = None,
               end_crawl_date: Optional[str] = None, start_published_date: Optional[str] = None,
               end_published_date: Optional[str] = None, use_autoprompt: Optional[bool] = None,
               type: Optional[str] = None) -> SearchResponse:
        options = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        validate_search_options(options)
        request = {'query': query}
        request.update(to_camel_case(options))
        response = requests.post(f"{self.base_url}/search", json=request, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}. Message: {response.text}")
        results = [Result(**to_snake_case(result)) for result in response.json()["results"]]
        search_response = SearchResponse(results=results)
        search_response.api = self
        return search_response

    def find_similar(self, url: str, num_results: Optional[int] = None, include_domains: Optional[List[str]] = None,
                     exclude_domains: Optional[List[str]] = None, start_crawl_date: Optional[str] = None,
                     end_crawl_date: Optional[str] = None, start_published_date: Optional[str] = None,
                     end_published_date: Optional[str] = None) -> SearchResponse:
        options = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        validate_find_similar_options(options)
        request = {'url': url}
        request.update(to_camel_case(options))
        response = requests.post(f"{self.base_url}/findSimilar", json=request, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}. Message: {response.text}")
        results = [Result(**to_snake_case(result)) for result in response.json()["results"]]
        find_similar_response = SearchResponse(results=results)
        find_similar_response.api = self
        return find_similar_response

    def get_contents(self, ids: List[str]) -> GetContentsResponse:
        if len(ids) == 0:
            raise ValueError("ids cannot be empty")
        response = requests.get(f"{self.base_url}/contents", params=to_camel_case({"ids": ids}), headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}. Message: {response.text}")
        return GetContentsResponse([DocumentContent(**to_snake_case(document)) for document in response.json()["contents"]])
