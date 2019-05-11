import pytest
import mock
from thesaurus import Thesaurus

@pytest.mark.unit
def test_can_populate_lookup_dict_correctly():
    mock_synonym_file = mock.MagicMock()
    mock_synonym_file.__enter__.return_value = [
        'rUn SPRINT jOg'
    ]
    thesaurus = Thesaurus(mock_synonym_file)
    assert thesaurus.lookup_dict == {
        'run': 'run',
        'sprint': 'run',
        'jog': 'run'
    }

@pytest.mark.unit
def test_can_get_synonym_correctly():
    mock_synonym_file = mock.MagicMock()
    mock_synonym_file.__enter__.return_value = [
        'rUn SPRINT jOg'
    ]
    thesaurus = Thesaurus(mock_synonym_file)
    assert thesaurus.get_synonym('RUN') == 'run'
    assert thesaurus.get_synonym('sprint') == 'run'
    assert thesaurus.get_synonym('jog') == 'run'
    assert thesaurus.get_synonym('LOL') == 'lol'
