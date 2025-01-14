from typing import List, Optional

from ..abstract import (
    AbstractQueryBuilder,
    ExtractionQuery,
    TimeFilter,
    WarehouseAsset,
)


class RedshiftQueryBuilder(AbstractQueryBuilder):
    """
    Builds queries to extract assets from Redshift.
    """

    def __init__(
        self,
        time_filter: Optional[TimeFilter] = None,
    ):
        super().__init__(time_filter=time_filter)

    def build(self, asset: WarehouseAsset) -> List[ExtractionQuery]:
        query = self.build_default(asset)
        return [query]
