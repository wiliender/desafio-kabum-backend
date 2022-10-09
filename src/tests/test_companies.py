import pytest

from data import companies

class TestCompanies:
    def setUp(self):
        # mocking "database" data
        companies._calc_shipping = [  # type: ignore "private" warning
            companies.Company(
                name="Entrega Ninja",
                deadline=6,
                shipping=0.3,
                min_height=10,
                max_height=200,
                min_width=6,
                max_width=140,
            ),
            companies.Company(
                name="Entrega KaBum",
                deadline=4,
                shipping=0.2,
                min_height=5,
                max_height=140,
                min_width=13,
                max_width=125,)]

    @pytest.mark.parametrize(
        "weight, k, expected",
        [(400, .3, 12), (300, .3, 9), (100, .3, 3), (5, .3, .15), (5, .2, .1), (7, .2, .14)])
    def test_shipping_calc(self, weight: float, k: float, expected: float):
        assert companies._calc_shipping(weight, k) == expected  # type: ignore

    @pytest.mark.parametrize(
        "height, width, weight, expected",
        [
            (102, 40, 400, [
                companies.CompanyResult("Entrega Ninja", 12, 6),
                companies.CompanyResult("Entrega KaBum", 8, 4)]),
            (102, 10, 400, [companies.CompanyResult("Entrega Ninja", 12, 6)]),
            (5, 13, 300, [companies.CompanyResult("Entrega KaBum", 6, 4)]),
            (199, 140, 100, []),
            (199, 4, 100, []),
            (199, 139, 100, [companies.CompanyResult("Entrega Ninja", 3, 6)]),
            (5, 124, 100, [companies.CompanyResult("Entrega KaBum", 2, 4)])])
    def test_get(
        self,
        width: float,
        height: float,
        weight: float,
        expected: list[companies.CompanyResult],
    ):
        res = companies.get(width, height, weight)
        assert res == expected
