from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from app import sqlalchemy as db


class Tenant(db.Model):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True)
    tenant_name = Column(String(255), nullable=False)
    tenant_code = Column(String(255))
    tenant_main_unit_no = Column(String(255))
    tenant_property_name = Column(String(255))
    tenant_general_contact = Column(String(255))
    tenant_telephone = Column(String(255))
    tenant_lease_start_date = Column(Date)
    tenant_lease_end_date = Column(Date)
    tenant_vacate_date = Column(Date)
    tenant_is_active = Column(Boolean, nullable=False, default=False)
    transactions = relationship("TenantTransaction")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @property
    def serialize(self):
        return {
            "id": self.id,
            "tenant_name": self.tenant_name,
            "tenant_code": self.tenant_code,
            "tenant_main_unit_no": self.tenant_main_unit_no,
            "tenant_property_name": self.tenant_property_name,
            "tenant_general_contact": self.tenant_general_contact,
            "tenant_telephone": self.tenant_telephone,
            "tenant_lease_start_date": self.tenant_lease_start_date,
            "tenant_lease_end_date": self.tenant_lease_end_date,
            "tenant_vacate_date": self.tenant_vacate_date,
            "tenant_is_active": self.tenant_is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "transactions": [txn.serialize for txn in self.transactions],
        }


class TenantTransaction(db.Model):
    __tablename__ = "tenant_transactions"
    id = Column(Integer, primary_key=True)
    period = Column(String(255), nullable=False)
    date = Column(Date)
    transaction = Column(String(255))
    tax = Column(Numeric(precision=10, scale=2))
    remarks = Column(String(255))
    exclusive = Column(Numeric(precision=10, scale=2))
    inclusive = Column(Numeric(precision=10, scale=2))
    description = Column(String(255))
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "period": self.period,
            "date": self.date,
            "transaction": self.transaction,
            "tax": float(self.tax),
            "remarks": self.remarks,
            "exclusive": float(self.exclusive),
            "inclusive": float(self.inclusive),
            "description": self.description,
            "tenant_id": self.tenant_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
