from dataclasses import dataclass


@dataclass
class LoginData:
    email: str = None
    password: str = None
