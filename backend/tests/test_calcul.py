import pytest
from backend.modules.calcul import carre

def test_carre_valid():
    assert carre(2) == 4
    assert carre(0) == 0
    assert carre(-3) == 9

def test_carre_invalid_type():
    with pytest.raises(TypeError):
        carre("a")
    with pytest.raises(TypeError):
        carre(2.5)
