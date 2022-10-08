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
