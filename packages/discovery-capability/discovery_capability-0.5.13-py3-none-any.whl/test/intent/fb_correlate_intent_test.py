import unittest
import os
from pathlib import Path
import shutil
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
from ds_capability import FeatureBuild
from ds_capability.intent.feature_build_intent import FeatureBuildIntentModel
from aistac.properties.property_manager import PropertyManager

# Pandas setup
pd.set_option('max_colwidth', 320)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 99)
pd.set_option('expand_frame_repr', True)


class FeatureBuilderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # clean out any old environments
        for key in os.environ.keys():
            if key.startswith('HADRON'):
                del os.environ[key]
        # Local Domain Contract
        os.environ['HADRON_PM_PATH'] = os.path.join('working', 'contracts')
        os.environ['HADRON_PM_TYPE'] = 'parquet'
        # Local Connectivity
        os.environ['HADRON_DEFAULT_PATH'] = Path('working/data').as_posix()
        # Specialist Component
        try:
            os.makedirs(os.environ['HADRON_PM_PATH'])
        except OSError:
            pass
        try:
            os.makedirs(os.environ['HADRON_DEFAULT_PATH'])
        except OSError:
            pass
        try:
            shutil.copytree('../_test_data', os.path.join(os.environ['PWD'], 'working/source'))
        except OSError:
            pass
        PropertyManager._remove_all()

    def tearDown(self):
        try:
            shutil.rmtree('working')
        except OSError:
            pass

    def test_for_smoke(self):
        fb = FeatureBuild.from_memory()
        tools: FeatureBuildIntentModel = fb.tools
        tbl = tools.get_synthetic_data_types(100)
        self.assertEqual((100, 6), tbl.shape)

    def test_correlate_discrete_intervals(self):
        fb = FeatureBuild.from_memory()
        tools: FeatureBuildIntentModel = fb.tools
        tbl = tools.get_synthetic_data_types(100)
        result = tools.correlate_discrete_intervals(tbl, header='num', column_name='num')
        self.assertEqual(3, pc.count(result.column('num').combine_chunks().dictionary).as_py())
        result = tools.correlate_discrete_intervals(tbl, header='num', categories=['low', 'mid', 'high'], column_name='num')
        self.assertCountEqual(['high', 'mid', 'low'], result.column('num').combine_chunks().dictionary.to_pylist())
        result = tools.correlate_discrete_intervals(tbl, header='num', granularity=[0.25,0.5,0.75],
                                                    categories=['0%->25%', '25%->50%', '50%->75%', '75%->100%'], column_name='num')
        self.assertCountEqual(['0%->25%', '25%->50%', '50%->75%', '75%->100%'], result.column('num').combine_chunks().dictionary.to_pylist())

    def test_correlate_on_condition(self):
        fb = FeatureBuild.from_memory()
        tools: FeatureBuildIntentModel = fb.tools
        tbl = tools.get_synthetic_data_types(1000, seed=101)
        # check no zeros
        self.assertEqual(0, pc.count(pc.index_in(tbl.column('int').combine_chunks(), pa.array([0])).drop_null()).as_py())
        # check three zeros
        result = tools.correlate_on_condition(tbl, header='int', other='num',
                                              condition=[(1, 'greater', 'or'), (-1, 'less', None)], value=0, column_name='int')
        self.assertEqual(352, pc.count(pc.index_in(result.column('int').combine_chunks(), pa.array([0])).drop_null()).as_py())
        # check string
        result = tools.correlate_on_condition(tbl, header='cat', other='cat',
                                              condition=[(pa.array(['INACTIVE', "SUSPENDED"]), 'is_in', None)], value='N/A', column_name='target')
        self.assertEqual(228, pc.count(pc.index_in(result.column('target').combine_chunks(), pa.array(['N/A'])).drop_null()).as_py())
        # check headers
        result = tools.correlate_on_condition(tbl, header='int', other='num',
                                              condition=[(1, 'greater', 'or'), (-1, 'less', None)],
                                              value=0, default=1, column_name='target')
        self.assertEqual(648, pc.sum(result.column('target')).as_py())
        result = tools.correlate_on_condition(tbl, header='int', other='num',
                                              condition=[(1, 'greater', 'or'), (-1, 'less', None)],
                                              value=0, default="@num", column_name='target')
        self.assertEqual(result.column('target').slice(2, 4), result.column('num').slice(2, 4))
        self.assertEqual(352, pc.count(pc.index_in(result.column('target').combine_chunks(), pa.array([0])).drop_null()).as_py())

    def test_correlate_column_join(self):
        fb = FeatureBuild.from_memory()
        tools: FeatureBuildIntentModel = fb.tools
        tbl = tools.get_synthetic_data_types(10, seed=101)
        result = tools.correlate_column_join(tbl, header='cat', others='string', sep=': ', column_name='compound')
        self.assertCountEqual(['cat', 'num', 'int', 'bool', 'date', 'compound'], result.column_names)
        self.assertEqual("PENDING: Smokeys Gate", result.column('compound').combine_chunks()[0].as_py())
        result = tools.correlate_column_join(tbl, header='cat', others='string', sep=': ', column_name='cat')
        self.assertCountEqual(['cat', 'num', 'int', 'bool', 'date'], result.column_names)
        self.assertEqual("PENDING: Smokeys Gate", result.column('cat').combine_chunks()[0].as_py())
        tbl = tools.get_synthetic_data_types(1000, inc_nulls=True, seed=101)
        result = tools.correlate_column_join(tbl, header='cat', others=['cat_null', 'string_null'], sep='-', column_name='compound')
        self.assertGreater(result.column('compound').combine_chunks().null_count, 0)




    def test_raise(self):
        with self.assertRaises(KeyError) as context:
            env = os.environ['NoEnvValueTest']
        self.assertTrue("'NoEnvValueTest'" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
