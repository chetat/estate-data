from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models import Tenant
from app.repository.base import AbstractRepository


class TenantRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id) -> Tenant | None:
        item = self.session.query(Tenant).filter_by(id=id).first()
        if not item:
            return None
        return item.serialize

    def add(self, tenant: Tenant):
        try:
            self.session.add(tenant)
            self.session.flush()
        except SQLAlchemyError as err:
            print(err)
            raise err
