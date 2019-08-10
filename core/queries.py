
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
    "from": None, "size": 10,
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

primary_category_search = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "should": [
                {
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
            ],
            "filter": {
                "term": {
                    "primary_category": None
                }
            }
        }
    }
}

#----------------------------------------Advanced Search APIs------------------------------------------#
# Search for authors

search_author = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "authors": None
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

# Search for Title

search_title = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "title": None
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

# Search for Abstract

search_abstract = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "abstract": None
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


# Search for Arxiv_id

search_arxiv = {
    "from": None, "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "arxiv_id": None
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
