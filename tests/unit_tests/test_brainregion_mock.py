from unittest.mock import MagicMock
from app.models import BrainRegion

def test_brainregion_repr():
    region = BrainRegion(id=1, name="Cortex", description="Test", function="Thinking")
    assert repr(region) == "<BrainRegion Cortex>"

def test_query_mocking():
    mock_region = MagicMock()
    mock_region.name = "Mocked"

    # Simulate what BrainRegion.query.get(id) would return
    mock_query = MagicMock()
    mock_query.get.return_value = mock_region

    result = mock_query.get(1)
    assert result.name == "Mocked"