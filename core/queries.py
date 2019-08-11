from gunicorn.six import advance_iterator

# A reservoir to maintain the various queries used in the search APIs


# This query fetch papers based on primary categories we have on researchkernel, with filterable dates and pagination.

get_primary_category_query = {
    "from": None, "size": 10,
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

get_sub_category_query = {
    "from": None, "size": 10,
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
    "from": None, "size": 10,
    "query": {
        "match": {
            "created": None,
        }
    }
}

#----------------------------------------Universal Search APIs----------------------------------------#

universal_search = {
    "from": 0, "size": 10,
    "query": {
        "multi_match": {
            "query": None,
            "type": "cross_fields",
            "fields": [
                "arxiv_id",
                "abstract",
                "title",
                "abstract",
                "authors",
                "doi"
            ]
        }
    }
}
#----------------------------------------Advanced Search APIs------------------------------------------#
# Search for any one field at at time.
advance_search = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        # add any number of field for filtering results here

                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "created": {
                            "gte": None,
                            "lte": None,
                            "format": "yyyy-MM-dd"
                        }
                    }
                }
            ]
        }
    }
}
