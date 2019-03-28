
DB_STRUCTURE = {
  "mappings": {
    "papers": {
      "properties": {
        "abstract": {
          "type": "text"
        },
        "arxiv_id": {
          "type": "text"
        },
        "authors": {
          "type": "text"
        },
        "categories": {
          "type": "text"
        },
        "created": {
          "type": "date",
          "format": "yyyy-MM-dd"
        },
        "doi": {
          "type": "text"
        },
        "primary category": {
          "type": "keyword"
        },
        "primary_category": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "title": {
          "type": "text"
        },
        "updated": {
          "type": "text"
        }
      }
    }
  }
}

SEARCH_URL = '_search'
