import inspect
import pandas as pd
import pyarrow as pa
from ds_capability.components.discovery import DataDiscovery
from ds_capability.intent.abstract_feature_build_intent import AbstractFeatureBuildIntentModel
from ds_capability.intent.common_intent import CommonsIntentModel
from ds_capability.components.commons import Commons
from ds_capability.managers.feature_build_property_manager import FeatureBuildPropertyManager


# noinspection PyArgumentList
class FeatureBuildModelIntent(AbstractFeatureBuildIntentModel, CommonsIntentModel):

    def __init__(self, property_manager: FeatureBuildPropertyManager, default_save_intent: bool=None,
                 default_intent_level: [str, int, float]=None, order_next_available: bool=None,
                 default_replace_intent: bool=None):
        """initialisation of the Intent class.

        :param property_manager: the property manager class that references the intent contract.
        :param default_save_intent: (optional) The default action for saving intent in the property manager
        :param default_intent_level: (optional) the default level intent should be saved at
        :param order_next_available: (optional) if the default behaviour for the order should be next available order
        :param default_replace_intent: (optional) the default replace existing intent behaviour
        """
        default_save_intent = default_save_intent if isinstance(default_save_intent, bool) else True
        default_replace_intent = default_replace_intent if isinstance(default_replace_intent, bool) else True
        default_intent_level = default_intent_level if isinstance(default_intent_level, (str, int, float)) else 'A'
        default_intent_order = -1 if isinstance(order_next_available, bool) and order_next_available else 0
        super().__init__(property_manager=property_manager, default_save_intent=default_save_intent,
                         default_intent_level=default_intent_level, default_intent_order=default_intent_order,
                         default_replace_intent=default_replace_intent)
        self.label_gen = Commons.label_gen()

    def model_sample_link(self, canonical: pa.Table, other: [str, pa.Table], headers: list, replace: bool=None,
                          rename_map: [dict, list]=None, multi_map: dict=None, relative_freq: list=None, seed: int=None,
                          save_intent: bool=None, column_name: [int, str]=None, intent_order: int=None,
                          replace_intent: bool=None, remove_duplicates: bool=None) -> pa.Table:
        """ Takes a target dataset and samples from that target to the size of the canonical

        :param canonical: a pa.Table as the reference table
        :param other: a direct pa.Table or reference to a connector.
        :param headers: the headers to be selected from the other table
        :param rename_map: (optional) a direct (list) or named (dict) mapping to the headers names.
        :param multi_map: (optional) multiple columns from a single e.g. {new_name: name} where name is copied new_name
        :param replace: (optional) assuming other is bigger than canonical, selects without replacement when True
        :param relative_freq: (optional) a weighting pattern of the selected data
        :param seed: (optional) a seed value for the random function: default to None
        :param save_intent: (optional) if the intent contract should be saved to the property manager
        :param column_name: (optional) the column name that groups intent to create a column
        :param intent_order: (optional) the order in which each intent should run.
                    - If None: default's to -1
                    - if -1: added to a level above any current instance of the intent section, level 0 if not found
                    - if int: added to the level specified, overwriting any that already exist

        :param replace_intent: (optional) if the intent method exists at the level, or default level
                    - True - replaces the current intent method with the new
                    - False - leaves it untouched, disregarding the new intent

        :param remove_duplicates: (optional) removes any duplicate intent in any level that is identical
        :return: a pa.Table
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   column_name=column_name, intent_order=intent_order, replace_intent=replace_intent,
                                   remove_duplicates=remove_duplicates, save_intent=save_intent)
        # intent action
        canonical = self._get_canonical(canonical)
        other = self._get_canonical(other)
        headers = Commons.list_formatter(headers)
        replace = replace if isinstance(replace, bool) else True
        seed = self._seed() if seed is None else seed
        # build the distribution sizes
        if isinstance(relative_freq, list) and len(relative_freq) > 1:
            relative_freq = self._freq_dist_size(relative_freq=relative_freq, size=other.shape[0], seed=seed)
        else:
            relative_freq = None
        other = Commons.filter_columns(other, headers=headers).to_pandas()
        other = other.sample(n=canonical.shape[0], weights=relative_freq, random_state=seed, ignore_index=True,
                             replace=replace)
        if isinstance(rename_map, list) and len(rename_map) == len(headers):
            other.columns = rename_map
        elif isinstance(rename_map, dict):
            other.rename(mapper=rename_map, axis='columns', inplace=True)
        if isinstance(multi_map, dict):
            for k, v in multi_map.items():
                if v in other.columns:
                    other[k] = other[v]
        other = pa.Table.from_pandas(other)
        return Commons.table_append(canonical, other)

    def model_difference(self, canonical: pa.Table, other: [str, pa.Table], on_key: [str, list], drop_zero_sum: bool=None,
                         summary_connector: bool=None, flagged_connector: str=None, detail_connector: str=None,
                         unmatched_connector: str=None, seed: int=None, save_intent: bool=None,
                         column_name: [int, str]=None, intent_order: int=None, replace_intent: bool=None,
                         remove_duplicates: bool=None, **kwargs) -> pa.Table:
        """returns the difference between two canonicals, joined on a common and unique key.
        The ``on_key`` parameter can be a direct reference to the canonical column header or to an environment
        variable. If the environment variable is used ``on_key`` should be set to ``"${<<YOUR_ENVIRON>>}"`` where
        <<YOUR_ENVIRON>> is the environment variable name.

        If the ``flagged connector`` parameter is used, a report flagging mismatched left data with right data
        is produced for this connector where 1 indicate a difference and 0 they are the same. By default this method
        returns this report but if this parameter is set the original canonical returned. This allows a canonical
        pipeline to continue through the component while outputting the difference report.

        If the ``detail connector`` parameter is used, a detail report of the difference where the left and right
        values that differ are shown.

        If the ``unmatched connector`` parameter is used, the on_key's that don't match between left and right are
        reported

        :param canonical: a pa.Table as the reference table
        :param other: a direct pa.Table or reference to a connector.
        :param on_key: The name of the key that uniquely joins the canonical to others
        :param drop_zero_sum: (optional) drops rows and columns which has a total sum of zero differences
        :param summary_connector: (optional) a connector name where the summary report is sent
        :param flagged_connector: (optional) a connector name where the differences are flagged
        :param detail_connector: (optional) a connector name where the differences are shown
        :param unmatched_connector: (optional) a connector name where the unmatched keys are shown
        :param seed: (optional) this is a placeholder, here for compatibility across methods
        :param save_intent: (optional) if the intent contract should be saved to the property manager
        :param column_name: (optional) the column name that groups intent to create a column
        :param intent_order: (optional) the order in which each intent should run.
                    - If None: default's to -1
                    - if -1: added to a level above any current instance of the intent section, level 0 if not found
                    - if int: added to the level specified, overwriting any that already exist

        :param replace_intent: (optional) if the intent method exists at the level, or default level
                    - True - replaces the current intent method with the new
                    - False - leaves it untouched, disregarding the new intent

        :param remove_duplicates: (optional) removes any duplicate intent in any level that is identical
        :return: a pa.Table
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   column_name=column_name, intent_order=intent_order, replace_intent=replace_intent,
                                   remove_duplicates=remove_duplicates, save_intent=save_intent)
        # intent action
        canonical = self._get_canonical(canonical)
        other = self._get_canonical(other)
        seed = seed if isinstance(seed, int) else self._seed()
        drop_zero_sum = drop_zero_sum if isinstance(drop_zero_sum, bool) else False
        flagged_connector = self._extract_value(flagged_connector)
        summary_connector = self._extract_value(summary_connector)
        detail_connector = self._extract_value(detail_connector)
        unmatched_connector = self._extract_value(unmatched_connector)
        on_key = Commons.list_formatter(self._extract_value(on_key))
        left_diff = Commons.list_diff(canonical.column_names, other.column_names, symmetric=False)
        right_diff = Commons.list_diff(other.column_names, canonical.column_names, symmetric=False)
        # drop columns
        tbl_canonical = canonical.drop_columns(left_diff)
        tbl_other = other.drop_columns(right_diff)
        # pandas
        df_canonical = tbl_canonical.to_pandas()
        df_other = tbl_other.to_pandas()
        # sort
        df_canonical.sort_values(on_key, inplace=True)
        df_other.sort_values(on_key, inplace=True)
        df_other = df_other.loc[:, df_canonical.columns.to_list()]

        # unmatched report
        if isinstance(unmatched_connector, str):
            if self._pm.has_connector(unmatched_connector):
                left_merge = pd.merge(df_canonical, df_other, on=on_key, how='left', suffixes=('', '_y'), indicator=True)
                left_merge = left_merge[left_merge['_merge'] == 'left_only']
                left_merge = left_merge[left_merge.columns[~left_merge.columns.str.endswith('_y')]]
                right_merge = pd.merge(df_canonical, df_other, on=on_key, how='right', suffixes=('_y', ''), indicator=True)
                right_merge = right_merge[right_merge['_merge'] == 'right_only']
                right_merge = right_merge[right_merge.columns[~right_merge.columns.str.endswith('_y')]]
                unmatched = pd.concat([left_merge, right_merge], axis=0, ignore_index=True)
                unmatched = unmatched.set_index(on_key, drop=True).reset_index(drop=True)
                unmatched.insert(0, 'found_in', unmatched.pop('_merge'))
                handler = self._pm.get_connector_handler(unmatched_connector)
                handler.persist_canonical(pa.Table.from_pandas(unmatched), **kwargs)
            else:
                raise ValueError(f"The connector name {unmatched_connector} has been given but no Connect Contract added")

        # remove non-matching rows
        df = pd.merge(df_canonical, df_other, on=on_key, how='inner', suffixes=('_x', '_y'))
        df_x = df.filter(regex='(_x$)', axis=1)
        df_y = df.filter(regex='(_y$)', axis=1)
        df_x.columns = df_x.columns.str.removesuffix('_x')
        df_y.columns = df_y.columns.str.removesuffix('_y')
        # flag the differences
        diff = df_x.ne(df_y).astype(int)
        if drop_zero_sum:
            diff = diff.loc[(diff != 0).any(axis=1),(diff != 0).any(axis=0)]
        # add back the keys
        for n in range(len(on_key)):
            diff.insert(n, on_key[n], df[on_key[n]].iloc[diff.index])

        # detailed report
        if isinstance(detail_connector, str):
            if self._pm.has_connector(detail_connector):
                diff_comp = df_x.astype(str).compare(df_y.astype(str)).fillna('-')
                for n in range(len(on_key)):
                    diff_comp.insert(n, on_key[n], df[on_key[n]].iloc[diff_comp.index])
                diff_comp.columns = ['_'.join(col) for col in diff_comp.columns.values]
                diff_comp.columns = diff_comp.columns.str.replace(r'_self$', '_x', regex=True)
                diff_comp.columns = diff_comp.columns.str.replace(r'_other$', '_y', regex=True)
                diff_comp.columns = diff_comp.columns.str.replace(r'_$', '', regex=True)
                diff_comp = diff_comp.sort_values(on_key)
                diff_comp = diff_comp.reset_index(drop=True)
                handler = self._pm.get_connector_handler(detail_connector)
                handler.persist_canonical(pa.Table.from_pandas(diff_comp), **kwargs)
            else:
                raise ValueError(f"The connector name {detail_connector} has been given but no Connect Contract added")

        # summary report
        if isinstance(summary_connector, str):
            if self._pm.has_connector(summary_connector):
                summary = diff.drop(on_key, axis=1).sum().reset_index()
                summary.columns = ['Attribute', 'Summary']
                summary = summary.sort_values(['Attribute'])
                indicator = pd.merge(df_canonical[on_key], df_other[on_key], on=on_key, how='outer', indicator=True)
                count = indicator['_merge'].value_counts().to_frame().reset_index().replace('both', 'matching')
                count.columns = ['Attribute', 'Summary']
                summary = pd.concat([count, summary], axis=0).reset_index(drop=True)
                handler = self._pm.get_connector_handler(summary_connector)
                handler.persist_canonical(pa.Table.from_pandas(summary), **kwargs)
            else:
                raise ValueError(f"The connector name {summary_connector} has been given but no Connect Contract added")

        # flagged report
        if isinstance(flagged_connector, str):
            if self._pm.has_connector(flagged_connector):
                diff = diff.sort_values(on_key)
                diff = diff.reset_index(drop=True)
                handler = self._pm.get_connector_handler(flagged_connector)
                handler.persist_canonical(pa.Table.from_pandas(diff), **kwargs)
                return canonical
            raise ValueError(f"The connector name {flagged_connector} has been given but no Connect Contract added")

        if drop_zero_sum:
            diff = diff.sort_values(on_key)
            diff = diff.reset_index(drop=True)

        return pa.Table.from_pandas(diff)

    def model_profiling(self, canonical: pa.Table, profiling: str, headers: [str, list]=None, d_types: [str, list]=None,
                        regex: [str, list]=None, drop: bool=None, connector_name: str=None,  seed: int=None,
                        save_intent: bool=None, column_name: [int, str]=None, intent_order: int=None,
                        replace_intent: bool=None, remove_duplicates: bool=None, **kwargs) -> pa.Table:
        """ Data profiling provides, analyzing, and creating useful summaries of data. The process yields a high-level
        overview which aids in the discovery of data quality issues, risks, and overall trends. It can be used to
        identify any errors, anomalies, or patterns that may exist within the data. There are three types of data
        profiling available 'dictionary', 'schema' or 'quality'

        :param canonical: a direct or generated pd.DataFrame. see context notes below
        :param profiling: The profiling name. Options are 'dictionary', 'schema' or 'quality'
        :param headers: (optional) a filter of headers from the 'other' dataset
        :param drop: (optional) to drop or not drop the headers if specified
        :param d_types: (optional) a filter on data type for the 'other' dataset. int, float, bool, object
        :param regex: (optional) a regular expression to search the headers. example '^((?!_amt).)*$)' excludes '_amt'
        :param connector_name::(optional) a connector name where the outcome is sent
        :param seed:(optional) this is a placeholder, here for compatibility across methods
        :param save_intent: (optional) if the intent contract should be saved to the property manager
        :param column_name: (optional) the column name that groups intent to create a column
        :param intent_order: (optional) the order in which each intent should run.
                    - If None: default's to -1
                    - if -1: added to a level above any current instance of the intent section, level 0 if not found
                    - if int: added to the level specified, overwriting any that already exist

        :param replace_intent: (optional) if the intent method exists at the level, or default level
                    - True - replaces the current intent method with the new
                    - False - leaves it untouched, disregarding the new intent

        :param remove_duplicates: (optional) removes any duplicate intent in any level that is identical
        :return: a pa.Table
        """
        # intent persist options
        self._set_intend_signature(self._intent_builder(method=inspect.currentframe().f_code.co_name, params=locals()),
                                   column_name=column_name, intent_order=intent_order, replace_intent=replace_intent,
                                   remove_duplicates=remove_duplicates, save_intent=save_intent)
        # intent action
        canonical = self._get_canonical(canonical)
        columns = Commons.filter_headers(canonical, headers=headers, d_types=d_types, regex=regex, drop=drop)
        _seed = self._seed() if seed is None else seed
        if profiling == 'dictionary':
            result =  DataDiscovery.data_dictionary(canonical=canonical, table_cast=True, stylise=False)
        elif profiling == 'quality':
            result =  DataDiscovery.data_quality(canonical=canonical, stylise=False)
        elif profiling == 'schema':
            result = DataDiscovery.data_schema(canonical=canonical, stylise=False)
        else:
            raise ValueError(f"The report name '{profiling}' is not recognised. Use 'dictionary', 'schema' or 'quality'")
        if isinstance(connector_name, str):
            if self._pm.has_connector(connector_name):
                handler = self._pm.get_connector_handler(connector_name)
                handler.persist_canonical(result, **kwargs)
                return canonical
            raise ValueError(f"The connector name {connector_name} has been given but no Connect Contract added")
        return result

