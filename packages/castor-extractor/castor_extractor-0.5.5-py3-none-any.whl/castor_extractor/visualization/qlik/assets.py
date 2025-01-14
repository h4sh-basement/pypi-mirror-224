from enum import Enum
from typing import Dict, Tuple


class QlikAsset(Enum):
    """Qlik assets"""

    SPACES = "spaces"
    USERS = "users"
    APPS = "apps"
    LINEAGE = "lineage"
    MEASURES = "measures"
    CONNECTIONS = "connections"


EXPORTED_FIELDS: Dict[QlikAsset, Tuple[str, ...]] = {
    QlikAsset.SPACES: (
        "id",
        "type",
        "ownerId",
        "tenantId",
        "name",
        "description",
        "meta",
        "links",
        "createdAt",
        "createdBy",
        "updatedAt",
    ),
    QlikAsset.USERS: (
        "id",
        "tenantId",
        "status",
        "name",
        "email",
        "links",
    ),
    QlikAsset.APPS: (
        "name",
        "spaceId",
        "description",
        "thumbnailId",
        "resourceAttributes",
        "resourceCustomAttributes",
        "resourceUpdatedAt",
        "resourceType",
        "resourceId",
        "resourceCreatedAt",
        "id",
        "createdAt",
        "updatedAt",
        "creatorId",
        "updaterId",
        "tenantId",
        "isFavorited",
        "links",
        "actions",
        "collectionIds",
        "meta",
        "ownerId",
        "resourceReloadEndTime",
        "resourceReloadStatus",
        "resourceSize",
        "itemViews",
    ),
    QlikAsset.MEASURES: (
        "qInfo",
        "qMeta",
        "qData",
    ),
    QlikAsset.CONNECTIONS: (
        "id",
        "links",
        "privileges",
        "qArchitecture",
        "qConnectStatement",
        "qEngineObjectID",
        "qID",
        "qLogOn",
        "qName",
        "qType",
        "tenant",
    ),
}
