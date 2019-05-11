import pytest
from ntuple import Ntuple

@pytest.mark.unit
def test_can_add_value_to_ntuple():
    ntuple = Ntuple(3)
    ntuple.add(1)
    ntuple.add(2)
    ntuple.add(3)
    assert set(ntuple.value) == set([1, 2, 3])

@pytest.mark.unit
def test_cannot_add_more_than_size():
    ntuple = Ntuple(3)
    ntuple.add(1)
    ntuple.add(2)
    ntuple.add(3)
    with pytest.raises(ValueError):
        ntuple.add(4)

@pytest.mark.unit
def test_can_add_all():
    ntuple = Ntuple(4)
    ntuple.add(1)
    ntuple.add(2)
    ntuple.add_all([3, 4])
    assert set(ntuple.value) == set([1, 2, 3, 4])

@pytest.mark.unit
def test_cannot_add_all_than_size():
    ntuple = Ntuple(3)
    ntuple.add(1)
    ntuple.add(2)
    with pytest.raises(ValueError):
        ntuple.add_all([3, 4])

@pytest.mark.unit
def test_return_true_if_equal():
    ntuple_1 = Ntuple(3)
    ntuple_1.add(1)
    ntuple_1.add(2)
    ntuple_1.add(3)

    ntuple_2 = Ntuple(3)
    ntuple_2.add_all([1, 2, 3])
    assert ntuple_1 == ntuple_2
