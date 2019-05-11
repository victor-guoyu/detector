import pytest
import mock
from ntuple import NtupleFactory, Ntuple

@pytest.mark.unit
def test_can_get_ntuple_from_line():
    mock_thesaurus = mock.MagicMock()
    line = 'go for a run'
    mock_thesaurus.get_synonym.side_effect = line.split()
    factory = NtupleFactory(size=3, thesaurus=mock_thesaurus)
    ntuple_list =factory.get_ntuple_from_line(line)
    assert len(ntuple_list) == 2

    test_result = Ntuple(3)
    test_result.add_all(['go', 'for', 'a'])
    assert ntuple_list[0] == test_result

    test_result = Ntuple(3)
    test_result.add_all(['for', 'a', 'run'])
    assert ntuple_list[1] == test_result

@pytest.mark.unit
def test_can_get_ntuple_list_from_file():
    mock_thesaurus = mock.MagicMock()
    mock_file = mock.MagicMock()
    mock_file.__enter__.return_value = [
        'go for a run',
        'this is a new line'
    ]

    factory = NtupleFactory(size=3, thesaurus=mock_thesaurus)
    ntuple_list = factory.get_ntuple_list_from_file(mock_file)

    assert len(ntuple_list) == 5
