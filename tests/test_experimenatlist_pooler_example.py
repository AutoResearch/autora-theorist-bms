from autora.experimentalist.pooler.example_pooler import example_pool


def test():
    sample = example_pool(2.0)
    assert sample == 2.0
