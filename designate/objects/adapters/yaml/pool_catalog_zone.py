# Copyright 2023 inovex GmbH
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from designate import objects
from designate.objects.adapters.yaml import base


class PoolCatalogZoneYAMLAdapter(base.YAMLAdapter):
    ADAPTER_OBJECT = objects.PoolCatalogZone
    MODIFICATIONS = {
        'fields': {
            'catalog_zone_fqdn': {
                'read_only': False
            },
            'catalog_zone_refresh': {
                'read_only': False
            },
            'catalog_zone_tsig_key': {
                'read_only': False
            },
            'catalog_zone_tsig_algorithm': {
                'read_only': False
            },
        }
    }