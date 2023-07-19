from flask import jsonify

from app import sqlalchemy as db
from app.api import api
from app.repository.tenants import TenantRepository


@api.route("/tenants/<int:tenant_id>/transactions")
def get_tenant_transaction(tenant_id):
    tenant_repo = TenantRepository(db.session)
    tenant_info = tenant_repo.get(tenant_id)
    return jsonify(tenant_info)
