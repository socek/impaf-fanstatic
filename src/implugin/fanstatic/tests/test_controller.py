from mock import patch

from pytest import yield_fixture

from impaf.controller import Controller
from impaf.testing import ControllerFixture

from ..controller import FanstaticController


class MockedFanstaticController(Controller):

    def _create_context(self):
        self.context = {
            'context': True,
        }


class ExampleFanstaticController(
    FanstaticController,
    MockedFanstaticController,
):
    pass


class TestFanstaticController(ControllerFixture):

    def _cls_controller(self):
        return ExampleFanstaticController

    @yield_fixture
    def mResources(self):
        patcher = patch('implugin.fanstatic.controller.Resources')
        with patcher as mock:
            yield mock

    def test_create_context(self, controller, mResources):
        controller._create_context()

        assert controller.context == {
            'context': True,
            'need': mResources.return_value.need
        }
        mResources.assert_called_once_with()
