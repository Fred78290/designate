# Copyright 2016 Hewlett Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import designate.conf
from designate import objects
from designate.scheduler.filters import base


CONF = designate.conf.CONF


class FallbackFilter(base.Filter):
    """If there is no zones available to schedule to, this filter will insert
    the default_pool_id.

    .. note::

        This should be used as one of the last filters, if you want to preserve
        behavior from before the scheduler existed.
    """

    name = 'fallback'
    """Name to enable in the ``[designate:central:scheduler].filters`` option
    list
    """

    def filter(self, context, pools, zone):
        if not pools:
            pools = objects.PoolList()
            pools.append(
                objects.Pool(id=CONF['service:central'].default_pool_id)
            )
        return pools
