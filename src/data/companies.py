from dataclasses import dataclass

@dataclass
class Company:
    name: str
    shipping: float
    min_height: float
    max_height: float
    min_width: float
    max_width: float
    deadline: int

@dataclass
class CompanyResult:
    nome: str
    valor_frete: float
    prazo_dias: int

_companies: list[Company] = [
    Company(
        name="Entrega Ninja",
        shipping=0.3,
        min_height=10,
        max_height=200,
        min_width=6,
        max_width=140,
        deadline=6,
    ),
    Company(
        name="Entrega KaBum",
        shipping=0.2,
        min_height=5,
        max_height=140,
        min_width=13,
        max_width=125,
        deadline=4,
    ),
]

def _calc_shipping(weight: float, k: float):
    return round((weight * k)/10, 2) # Up to two decimal places

def get(width: float, height: float, weight: float) -> list[CompanyResult]:
    filterA = filter(
        lambda x: width < x.max_width and width >= x.min_width,
        _companies,
    )
    filterB = filter(
        lambda x: height < x.max_height and height >= x.min_height,
        filterA,
    )

    return [
        CompanyResult(
            nome=i.name,
            valor_frete=_calc_shipping(weight, i.shipping),
            prazo_dias=i.deadline,
        ) for i in filterB]