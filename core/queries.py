
# A reservoir to maintain the various queries used in the search APIs

abstract_primary_category_query = {
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
    "query": {
        "match": {
            "created": None,
        }
    }
}
