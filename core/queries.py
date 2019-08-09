
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

primary_category_search = {
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
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
    "from": 0, "size": 10,
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
