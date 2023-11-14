import dataclasses


@dataclasses.dataclass
class Hotel:
    name: str
    address: str
    type: str
    services_in_the_hotel: list
    services_in_the_room: list
    price_for_night: float
