from sqlmodel import Session

from app.core.models import Personage
from app.core.repository import IdType, Repository


class PersonageController(Repository[Personage]):
    def create(session: Session, item: Personage) -> None:
        session.add(item)

    def get_by_id(session: Session, id_: IdType) -> Personage | None:
        personage = session.get_one(Personage, id_)

        return personage

    def get_all(session: Session) -> list[Personage]:
        personages = session.get(Personage)

        return personages

    def delete(session: Session, id_: IdType) -> bool:
        personage = session.get_one(Personage, id_)

        if personage is None:
            return False

        session.delete(personage)

        return True
