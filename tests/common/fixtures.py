# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import pytest


ELASTICSEARCH_HOST = os.environ.get("ELASTICSEARCH_HOST", "http://localhost:9200")
ELASTICSEARCH_INDEX = "hypothesis-test"


@pytest.fixture(scope="session", autouse=True)
def init_elasticsearch():
    import elasticsearch
    from h.search import init, get_client

    client = get_client({
        "es.host": ELASTICSEARCH_HOST,
        "es.index": ELASTICSEARCH_INDEX,
    })

    # Delete the hypothes-test index, in case it was left over from a
    # previous test run.
    conn = elasticsearch.Elasticsearch([ELASTICSEARCH_HOST])
    if conn.indices.exists(index=ELASTICSEARCH_INDEX):
        conn.indices.delete(index=ELASTICSEARCH_INDEX)

    init(client)
