from uuid import UUID

class ProcessSaleError(Exception):

    def __init__(self, raw_sale_id: UUID, inner_exception: Exception = None):

        self.raw_sale_data_id = raw_sale_id
        self.inner_exception = inner_exception

