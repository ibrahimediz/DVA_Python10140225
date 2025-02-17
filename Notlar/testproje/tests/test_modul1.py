import pytest
def ornekTest():
    assert 1 == 1

@pytest.fixture
def ornek_veri():
    return [1,2,3]

def testornek1(ornek_veri):
    assert len(ornek_veri) == 3

@pytest.mark.parametrize("giris,cikis",[(1,2),(2,4),(3,6),])
def test_parametrized(giris,cikis):
    assert giris*2==cikis


