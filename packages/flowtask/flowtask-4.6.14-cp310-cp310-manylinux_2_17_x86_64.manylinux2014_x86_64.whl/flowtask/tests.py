import asyncio
from typing import Any
from abc import ABC
import pandas as pd
import pytest
from navconfig import BASE_DIR
from flowtask.components import getComponent
from flowtask.components.abstract import DtComponent

@pytest.fixture(autouse=True, scope='session')
def component():
    cp = 'Dummy'
    yield cp

pytestmark = pytest.mark.asyncio


class BaseTestCase(ABC):
    """BaseTestCase.

    Args:
        BoilerPlate for Testing Dataintegration Components.
    """
    arguments: dict = {}
    component = None
    name: str = None
    expected_result: Any = None
    expected_result_type: type = None

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, component):
        error = None
        self.name = component
        try:
            obj = getComponent(component)
            self.component = obj(**self.arguments)
        except Exception as e:
            print(e)
            error = e
        assert (not error)
        yield f"Starting Component {self.name}"

    def teardown_class(self):
        try:
            asyncio.run_until_complete(self.component.close())
        except Exception:
            pass
        self.component = None

    @pytest.fixture(autouse=True)
    def setup_method(self, component):
        self.name = component
        error = None
        try:
            obj = getComponent(component)
            self.component = obj(**self.arguments)
        except Exception as e:
            print(e)
            error = e
        assert (not error)

    def teardown_method(self):
        try:
            asyncio.run_until_complete(self.component.close())
        except Exception:
            pass
        self.component = None

    async def test_initialize(self, component):
        assert self.name == component
        assert isinstance(self.component, DtComponent) is True
        assert self.component.ComponentName() == component

    async def test_start(self):
        pytest.assume(self.component is not None)
        assert callable(self.component.start)
        if asyncio.iscoroutinefunction(self.component.start):
            start = await self.component.start()
        else:
            start = self.component.start()
        pytest.assume(start is True)
        if asyncio.iscoroutinefunction(self.component.close):
            await self.component.close()
        else:
            self.component.close()

    async def test_run(self):
        result = None
        error = None
        pytest.assume(self.component is not None)
        # start firsts:
        if asyncio.iscoroutinefunction(self.component.start):
            start = await self.component.start()
        else:
            start = self.component.start()
        try:
            if asyncio.iscoroutinefunction(self.component.run):
                result = await self.component.run()
            else:
                result = self.component.run()
            # print('RESULT : ', result)
            if self.expected_result is not None:
                pytest.assume(self.expected_result == result)
            if self.expected_result_type:
                pytest.assume(
                    isinstance(result, self.expected_result_type)
                )
        except Exception as e:
            error = e
        print('ERROR ', error)
        pytest.assume(result is not None)
        assert (error is None)
        if asyncio.iscoroutinefunction(self.component.close):
            await self.component.close()
        else:
            self.component.close()

    async def test_close(self):
        error = None
        pytest.assume(self.component is not None)
        # starts first:
        if asyncio.iscoroutinefunction(self.component.start):
            start = await self.component.start()
        else:
            start = self.component.start()
        try:
            if asyncio.iscoroutinefunction(self.component.close):
                await self.component.close()
            else:
                self.component.close()
        except Exception as e:
            error = e
        assert (error is None)

class PandasTestCase(BaseTestCase):
    """PandasTestCase.

    Args:
        Test Case for components that requires a previous Pandas Dataframe.
    """
    file_test: str = None
    renamed_cols: list = []

    def return_pandas(self):
        filepath = BASE_DIR.joinpath('docs', self.file_test)
        assert filepath.exists()
        df = pd.read_csv(filepath)
        assert df is not None
        return df

    @pytest.fixture(autouse=True)
    def setup_method(self, component):
        self.name = component
        error = None
        try:
            obj = getComponent(component)
            df = self.return_pandas()
            self.arguments['input_result'] = df
            self.component = obj(**self.arguments)
        except Exception as e:
            print(e)
            error = e
        assert (not error)

    async def test_start(self):
        pytest.assume(self.component is not None)
        assert callable(self.component.start)
        error = None
        try:
            await self.component.start()
        except Exception as err:
            error = err
        pytest.assume(error is None)
        if asyncio.iscoroutinefunction(self.component.close):
            await self.component.close()
        else:
            self.component.close()

    async def test_run(self):
        result = None
        error = None
        pytest.assume(self.component is not None)
        # start firsts:
        if asyncio.iscoroutinefunction(self.component.start):
            start = await self.component.start()
        else:
            start = self.component.start()
        pytest.assume(start is not False)
        try:
            if asyncio.iscoroutinefunction(self.component.run):
                result = await self.component.run()
            else:
                result = self.component.run()
            pytest.assume(isinstance(result, pd.DataFrame))
            if self.expected_result is not None:
                ## TODO: making proves of transformations
                pytest.assume(self.expected_result == result)
            if self.renamed_cols is not None:
                columns = result.columns.values.tolist()
                # check if those columns are present in Dataframe
                for col in self.renamed_cols:
                    pytest.assume(col in columns)
        except Exception as e:
            error = e
        print('ERROR :: ', error)
        pytest.assume(result is not None)
        assert (error is None)
        if asyncio.iscoroutinefunction(self.component.close):
            await self.component.close()
        else:
            self.component.close()

def pytest_sessionfinish(session, exitstatus):
    asyncio.get_event_loop().close()
