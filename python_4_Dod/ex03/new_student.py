import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Practicing creating class using dataclasses"""
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    _existing_logins = set()  # Class-level set to save all used login

    def __init__(self, name: str, surname: str):
        """Explicit constructor to restrict input"""
        self.name = name
        self.surname = surname
        self.active = True
        self.id = generate_id()

        # generating login with sequence number if repeated
        base_login = f"{self.name[0].upper()}{self.surname.lower()}"
        login = base_login
        count = 1

        while login in Student._existing_logins:
            login = f"{base_login}{count}"
            count += 1

        Student._existing_logins.add(login)
        self.login = login
