########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############


__author__ = 'dank'


import json
import pkgutil
from StringIO import StringIO


def get_version():
    version_data = get_version_data()
    return json.loads(version_data)['version']


def get_detailed_version():
    version_data = get_version_data()
    version = StringIO()
    version.write('Cloudify CLI {version}'.format(**version_data))
    if version_data['build']:
        version.write(' (build: {build}, date: {date})'.format(**version_data))
    return version.getvalue()


def get_version_data():
    data = pkgutil.get_data('cosmo_cli', 'VERSION')
    return json.loads(data)
