import dataclasses


@dataclasses.dataclass
class User:
    arrival_date: str
    departure_date: str
    destination_city: str
    destination_country: str
    count_room: int
    count_guests: int
