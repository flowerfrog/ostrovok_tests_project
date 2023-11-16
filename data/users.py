import dataclasses


@dataclasses.dataclass
class User:
    arrival_date: str
    departure_date: str
    destination_city: str
    destination_country: str
    count_room: int
    count_guests: int


@dataclasses.dataclass
class UserFeedback:
    name_user: str
    email_user: str
    hotel_name: str
    hotel_city: str
    hotel_country: str
    questions: str


