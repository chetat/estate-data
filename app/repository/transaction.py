from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models import TenantTransaction
from app.repository.base import AbstractRepository


class TenantTransactionRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id) -> TenantTransaction | None:
        try:
            tenant_transaction = (
                self.session.query(TenantTransaction).filter_by(id=id).first()
            )
        except SQLAlchemyError as err:
            print(err)
            raise err
        return tenant_transaction

    def add(self, tenant_transaction: TenantTransaction) -> TenantTransaction:
        try:
            self.session.add(tenant_transaction)
        except SQLAlchemyError as err:
            print(err)
            raise err
        return tenant_transaction

    def bulk_add(self, tenant_transactions: list[TenantTransaction]):
        try:
            self.session.bulk_save_objects(tenant_transactions)
        except SQLAlchemyError as err:
            print(err)
            raise err
        return tenant_transactions
