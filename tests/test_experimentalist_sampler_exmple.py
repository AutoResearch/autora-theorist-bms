from autora.experimentalist.sampler.example_sampler import example_sampler


def test():
    sample = example_sampler([2, 3])
    assert sample == 2
