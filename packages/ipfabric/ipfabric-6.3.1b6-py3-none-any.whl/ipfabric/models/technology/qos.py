import logging
from typing import Any

from pydantic import BaseModel

from ipfabric import models

logger = logging.getLogger("ipfabric")


class Qos(BaseModel):
    client: Any = None

    @property
    def policy_maps(self):
        return models.Table(client=self.client, endpoint="tables/qos/policy-maps")

    @property
    def shaping(self):
        return models.Table(client=self.client, endpoint="tables/qos/shaping")

    @property
    def queuing(self):
        return models.Table(client=self.client, endpoint="tables/qos/queuing")

    @property
    def policing(self):
        return models.Table(client=self.client, endpoint="tables/qos/policing")

    @property
    def priority_queuing(self):
        return models.Table(client=self.client, endpoint="tables/qos/priority-queuing")

    @property
    def marking(self):
        return models.Table(client=self.client, endpoint="tables/qos/marking")

    @property
    def random_drops(self):
        return models.Table(client=self.client, endpoint="tables/qos/random-drops")
