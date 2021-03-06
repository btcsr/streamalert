"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

from mock import patch
from moto import mock_ssm

from stream_alert.apps.main import handler
from tests.unit.stream_alert_apps.test_helpers import (
    get_event,
    get_mock_context,
    put_mock_params
)


@mock_ssm
@patch.dict(os.environ, {'AWS_DEFAULT_REGION': 'us-east-1'})
@patch('stream_alert.apps.app_base.AppIntegration.gather')
def test_handler(gather_mock):
    """StreamAlertApp Lambda - Test Handler"""
    app_type = 'duo_auth'
    event = get_event(app_type)
    put_mock_params(app_type)
    handler(event, get_mock_context(app_type))
    gather_mock.assert_called_once()
