from unittest import TestCase, main
from hypothesis import given
from hypothesis import strategies as st
from typing import Union
def div(x: int, y: int) -> Union[int, float]:
    return x / y

class TestDiv(TestCase):
    @given(st.integers(), st.integers().filter(lambda y: y != 0))
    def test_div_explodion(self, x, y):

        div(x,y)

if __name__ == '__main__':
    main()