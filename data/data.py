from dataclasses import dataclass


@dataclass
class GenInfo:
    firstname: str = None
    lastname: str = None
    username: str = None
    temperature_from: int = None
    temperature_to: int = None
    id_number: str = None
    email: str = None
    address: str = None
    mobile: str = None
    password: str = None
    address_buffalo: str = None
    universal: str = None
    year: int = None
