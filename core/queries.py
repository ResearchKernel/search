
# A reservoir to maintain the various queries used in the search APIs

abstract_primary_category_query = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "primary_category": None,
          },
        },
      ],
      "filter": [
        {
          "range": {
            "created": {
              "gte": None,
              "lte": None,
              "format": "yyyy-MM-dd",
            },
          },
        },
      ],
    },
  },
}

abstract_category_query = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "categories": None,
          },
        },
      ],
      "filter": [
        {
          "range": {
            "created": {
              "gte": None,
              "lte": None,
              "format": "yyyy-MM-dd",
            },
          },
        },
      ],
    },
  },
}

abstract_recent_query = {
  "query": {
    "match": {
      "created": None,
    }
  }
}