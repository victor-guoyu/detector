import pytest
import mock
from detector import Detector

@pytest.mark.unit
@pytest.mark.parametrize('synonym_file_content, input_1_content, input_2_content, expected_percentage', [
    (['run sprint jog'], ['go for a run'], ['go for a jog'], 100),
    (['run sprint jog'], ['go for a run'], ['went for a jog'], 50),
])
def test_can_calculate_percentage(synonym_file_content, input_1_content, input_2_content, expected_percentage):
    mock_synonym_file = mock.MagicMock()
    mock_synonym_file.__enter__.return_value = synonym_file_content
    mock_input_1 = mock.MagicMock()
    mock_input_1.__enter__.return_value = input_1_content
    mock_input_2 = mock.MagicMock()
    mock_input_2.__enter__.return_value = input_2_content

    detector = Detector(
        synonym_file=mock_synonym_file,
        input_file_1=mock_input_1,
        input_file_2=mock_input_2,
        tuple_size=3
    )
    assert detector.calculate_percentage() == expected_percentage
