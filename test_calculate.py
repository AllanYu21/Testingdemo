import pytest

@pytest.mark.parametrize("a, b, expected", [
							(2,3,5),
							(3,7,10),
							(-2, 5, 3),
							(2,10,11),
							(.1,.2,.3)
							])
def test_add(a,b,expected):
	from calculate import add
	result = add(a,b)
	assert result == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
							(2,3,-1),
							(3,7,-4),
							(-2, 5, -7),
							(2,10,11)
							])
def test_sub(a,b,expected):
	from calculate import sub
	result = sub(a,b)
	assert result == expected