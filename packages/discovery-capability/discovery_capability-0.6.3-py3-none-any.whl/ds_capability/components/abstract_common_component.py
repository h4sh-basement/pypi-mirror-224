from abc import abstractmethod
import pandas as pd
import pyarrow as pa
from ds_core.components.abstract_component import AbstractComponent

from ds_capability.components.commons import Commons

__author__ = 'Darryl Oatridge'

from ds_capability.components.discovery import DataDiscovery


class AbstractCommonComponent(AbstractComponent):

    DEFAULT_MODULE = 'ds_core.handlers.pyarrow_handlers'
    DEFAULT_SOURCE_HANDLER = 'PyarrowSourceHandler'
    DEFAULT_PERSIST_HANDLER = 'PyarrowPersistHandler'

    @classmethod
    @abstractmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, creator: str, uri_pm_repo: str=None, pm_file_type: str=None,
                 pm_module: str=None, pm_handler: str=None, pm_kwargs: dict=None, default_save=None,
                 reset_templates: bool=None, template_path: str=None, template_module: str=None,
                 template_source_handler: str=None, template_persist_handler: str=None, align_connectors: bool=None,
                 default_save_intent: bool=None, default_intent_level: bool=None, order_next_available: bool=None,
                 default_replace_intent: bool=None, has_contract: bool=None):
        return cls

    # @property
    # def discover(self) -> DataDiscovery:
    #     """The components instance"""
    #     return DataDiscovery()

    # @property
    # def visual(self) -> Visualisation:
    #     """The visualisation instance"""
    #     return Visualisation()

    def load_source_canonical(self, reset_changed: bool=None, has_changed: bool=None, return_empty: bool=None,
                              **kwargs) -> pa.Table:
        """returns the contracted source data as a DataFrame

        :param reset_changed: (optional) resets the has_changed boolean to True
        :param has_changed: (optional) tests if the underline canonical has changed since last load else error returned
        :param return_empty: (optional) if has_changed is set, returns an empty canonical if set to True
        :param kwargs: arguments to be passed to the handler on load
        """
        return self.load_canonical(self.CONNECTOR_SOURCE, reset_changed=reset_changed, has_changed=has_changed,
                                   return_empty=return_empty, **kwargs)

    def load_canonical(self, connector_name: str, reset_changed: bool=None, has_changed: bool=None,
                       return_empty: bool=None, **kwargs) -> pa.Table:
        """returns the canonical of the referenced connector

        :param connector_name: the name or label to identify and reference the connector
        :param reset_changed: (optional) resets the has_changed boolean to True
        :param has_changed: (optional) tests if the underline canonical has changed since last load else error returned
        :param return_empty: (optional) if has_changed is set, returns an empty canonical if set to True
        :param kwargs: arguments to be passed to the handler on load
        """
        canonical = super().load_canonical(connector_name=connector_name, reset_changed=reset_changed,
                                           has_changed=has_changed, return_empty=return_empty, **kwargs)
        return canonical

    def load_persist_canonical(self, reset_changed: bool=None, has_changed: bool=None, return_empty: bool=None,
                               **kwargs) -> pa.Table:
        """loads the clean pandas.DataFrame from the clean folder for this contract

        :param reset_changed: (optional) resets the has_changed boolean to True
        :param has_changed: (optional) tests if the underline canonical has changed since last load else error returned
        :param return_empty: (optional) if has_changed is set, returns an empty canonical if set to True
        :param kwargs: arguments to be passed to the handler on load
        """
        return self.load_canonical(self.CONNECTOR_PERSIST, reset_changed=reset_changed, has_changed=has_changed,
                                   return_empty=return_empty, **kwargs)

    def save_persist_canonical(self, canonical, auto_connectors: bool=None, **kwargs):
        """Saves the canonical to the clean files folder, auto creating the connector from template if not set"""
        if auto_connectors if isinstance(auto_connectors, bool) else True:
            if not self.pm.has_connector(self.CONNECTOR_PERSIST):
                self.set_persist()
        self.persist_canonical(connector_name=self.CONNECTOR_PERSIST, canonical=canonical, **kwargs)

    def add_column_description(self, column_name: str, description: str, save: bool=None):
        """ adds a description note that is included in with the 'report_column_catalog'"""
        if isinstance(description, str) and description:
            self.pm.set_intent_description(level=column_name, text=description)
            self.pm_persist(save)
        return

    @staticmethod
    def quality_report(canonical: pa.Table, nulls_threshold: float=None, dom_threshold: float=None,
                     cat_threshold: int=None, stylise: bool=None):
        """ Analyses a dataset, passed as a DataFrame and returns a quality summary

        :param canonical: The table to view.
        :param cat_threshold: (optional) The threshold for the max number of unique categories. Default is 60
        :param dom_threshold: (optional) The threshold limit of a dominant value. Default 0.98
        :param nulls_threshold: (optional) The threshold limit of a nulls value. Default 0.9
        :param stylise: (optional) if the output is stylised
        """
        stylise = stylise if isinstance(stylise, bool) else True
        return DataDiscovery.data_quality(canonical=canonical, nulls_threshold=nulls_threshold,
                                          dom_threshold=dom_threshold, cat_threshold=cat_threshold, stylise=stylise)
    @staticmethod
    def canonical_report(canonical: pa.Table, headers: [str,list]=None, regex:[str,list]=None, d_types:list=None,
                         drop: bool=None, stylise: bool=None, display_width: int=None):
        """The Canonical Report is a data dictionary of the canonical providing a reference view of the dataset's
        attribute properties

        :param canonical: the table to view
        :param headers: (optional) specific headers to display
        :param regex: (optional) specify header regex to display. regex matching is done using the Google RE2 library.
        :param d_types: (optional) a list of pyarrow DataType e.g [pa.string(), pa.bool_()]
        :param drop: (optional) if the headers are to be dropped and the remaining to display
        :param stylise: (optional) if True present the report stylised.
        :param display_width: (optional) the width of the observational display
        """
        stylise = stylise if isinstance(stylise, bool) else True
        tbl = Commons.filter_columns(canonical, headers=headers, regex=regex, d_types=d_types, drop=drop)
        return DataDiscovery.data_dictionary(canonical=tbl, stylise=stylise, display_width=display_width)

    @staticmethod
    def schema_report(canonical: pa.Table, headers: [str,list]=None, regex:[str,list]=None, d_types:list=None,
                      drop: bool=None, stylise: bool=True, table_cast: bool=None):
        """ presents the current canonical schema

        :param canonical: the table to view
        :param headers: (optional) specific headers to display
        :param regex: (optional) specify header regex to display. regex matching is done using the Google RE2 library.
        :param d_types: (optional) a list of pyarrow DataType e.g [pa.string(), pa.bool_()]
        :param drop: (optional) if the headers are to be dropped and the remaining to display
        :param stylise: (optional) if True present the report stylised.
        :param table_cast: (optional) if the column should try to be cast to its type
        """
        stylise = stylise if isinstance(stylise, bool) else True
        table_cast = table_cast if isinstance(table_cast,bool) else True
        tbl = Commons.filter_columns(canonical, headers=headers, regex=regex, d_types=d_types, drop=drop)
        return DataDiscovery.data_schema(canonical=tbl, table_cast=table_cast, stylise=stylise)

    def report_task(self, stylise: bool=True):
        """ generates a report on the source contract

        :param stylise: (optional) returns a stylised DataFrame with formatting
        :return: pd.DataFrame
        """
        report = self.pm.report_task_meta()
        df = pd.DataFrame.from_dict(data=report, orient='index').reset_index()
        df.columns = ['name', 'value']
        # sort out any values that start with a $ as it throws formatting
        for c in df.columns:
            df[c] = [f"{x[1:]}" if str(x).startswith('$') else x for x in df[c]]
        if stylise:
            return Commons.report(df, index_header='name')
        return df

    def report_connectors(self, connector_filter: [str, list]=None, inc_pm: bool=None, inc_template: bool=None,
                          stylise: bool=True):
        """ generates a report on the source contract

        :param connector_filter: (optional) filters on the connector name.
        :param inc_pm: (optional) include the property manager connector
        :param inc_template: (optional) include the template connectors
        :param stylise: (optional) returns a stylised DataFrame with formatting
        :return: pd.DataFrame
        """
        report = self.pm.report_connectors(connector_filter=connector_filter, inc_pm=inc_pm,
                                           inc_template=inc_template)
        df = pd.DataFrame.from_dict(data=report)
        # sort out any values that start with a $ as it throws formatting
        for c in df.columns:
            df[c] = [f"{x[1:]}" if str(x).startswith('$') else x for x in df[c]]
        if stylise:
            return Commons.report(df, index_header='connector_name')
        return df

    def report_column_catalog(self, column_name: [str, list]=None, stylise: bool=True):
        """ generates a report on the source contract

        :param column_name: (optional) filters on specific column names.
        :param stylise: (optional) returns a stylised DataFrame with formatting
        :return: pd.DataFrame
        """
        stylise = True if not isinstance(stylise, bool) else stylise
        style = [{'selector': 'th', 'props': [('font-size', "120%"), ("text-align", "center")]},
                 {'selector': '.row_heading, .blank', 'props': [('display', 'none;')]}]
        df = pd.DataFrame.from_dict(data=self.pm.report_intent(levels=column_name, as_description=True,
                                                               level_label='column_name'))
        if stylise:
            df_style = df.style.set_table_styles(style).set_properties(**{'text-align': 'left'})
            _ = df_style.set_properties(subset=['column_name'], **{'font-weight': 'bold'})
            return df_style
        return df

    def report_run_book(self, stylise: bool=True):
        """ generates a report on all the intent

        :param stylise: returns a stylised dataframe with formatting
        :return: pd.Dataframe
        """
        df = pd.DataFrame.from_dict(data=self.pm.report_run_book())
        if stylise:
            return Commons.report(df, index_header='name')
        return df

    def report_environ(self, hide_not_set: bool=True, stylise: bool=True):
        """ generates a report on all the intent

        :param hide_not_set: hide environ keys that are not set.
        :param stylise: returns a stylised dataframe with formatting
        :return: pd.Dataframe
        """
        df = pd.DataFrame.from_dict(data=super().report_environ(hide_not_set), orient='index').reset_index()
        df.columns = ["environ", "value"]
        if stylise:
            return Commons.report(df, index_header='environ')
        return df

    def report_intent(self, levels: [str, int, list]=None, stylise: bool=True):
        """ generates a report on all the intent

        :param levels: (optional) a filter on the levels. passing a single value will report a single parameterised view
        :param stylise: (optional) returns a stylised dataframe with formatting
        :return: pd.Dataframe
        """
        if isinstance(levels, (int, str)):
            df = pd.DataFrame.from_dict(data=self.pm.report_intent_params(level=levels))
            if stylise:
                return Commons.report(df, index_header='order')
        df = pd.DataFrame.from_dict(data=self.pm.report_intent(levels=levels))
        if stylise:
            return Commons.report(df, index_header='level')
        return df

    def report_notes(self, catalog: [str, list]=None, labels: [str, list]=None, regex: [str, list]=None,
                     re_ignore_case: bool=False, stylise: bool=True, drop_dates: bool=False):
        """ generates a report on the notes

        :param catalog: (optional) the catalog to filter on
        :param labels: (optional) s label or list of labels to filter on
        :param regex: (optional) a regular expression on the notes
        :param re_ignore_case: (optional) if the regular expression should be case sensitive
        :param stylise: (optional) returns a stylised dataframe with formatting
        :param drop_dates: (optional) excludes the 'date' column from the report
        :return: pd.Dataframe
        """
        report = self.pm.report_notes(catalog=catalog, labels=labels, regex=regex, re_ignore_case=re_ignore_case,
                                      drop_dates=drop_dates)
        df = pd.DataFrame.from_dict(data=report)
        if stylise:
            return Commons.report(df, index_header='section', bold='label')
        return df
