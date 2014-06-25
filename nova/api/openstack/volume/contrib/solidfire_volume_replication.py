# Copyright (c) 2012 SolidFire, Inc.
# All Rights Reserved.
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

"""The SolidFire Volume Replication API extension."""


from nova.api.openstack import extensions
from nova import flags
from nova.compute import api as compute_api
from nova import log as logging
from nova.volume.san import SolidFireSanISCSIDriver as solidfire

LOG = logging.getLogger(__name__)
authorize = extensions.extension_authorizer('volume', 'solidfire_volume_replication')

FLAGS = flags.FLAGS

def _get_context(req):
    return req.environ['nova.context']


class SolidfireController(object):
    """The SolidFire Replication API controller for the OpenStack API."""
    def __init__(self):
        self.api = compute_api.AggregateAPI()

    def index(self, req):
        import pdb;pdb.set_trace()
        return None

class Solidfire_volume_replication(extensions.ExtensionDescriptor):
    """Foo administration"""

    name = "Solidfire_volume_replication"
    alias = "os-solidfire-volume-replication"
    namespace = "http://docs.openstack.org/compute/ext/solidfire-volume-replication/api/v1.1"
    updated = "2012-01-12T00:00:00+00:00"

    def __init__(self, ext_mgr):
        ext_mgr.register(self)

    def get_resources(self):
        resources = []
        res = extensions.ResourceExtension('os-solidfire-volume-replication',
                                           SolidfireController(),
                                           member_actions={"action": "POST", })
        resources.append(res)
        return resources
