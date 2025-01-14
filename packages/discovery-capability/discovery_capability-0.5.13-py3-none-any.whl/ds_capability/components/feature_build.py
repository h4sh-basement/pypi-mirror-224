from __future__ import annotations

from typing import Any

from ds_capability.intent.feature_build_intent import FeatureBuildIntentModel
from ds_capability.managers.feature_build_property_manager import FeatureBuildPropertyManager
from ds_capability.components.abstract_common_component import AbstractCommonComponent

__author__ = 'Darryl Oatridge'


class FeatureBuild(AbstractCommonComponent):

    @classmethod
    def from_uri(cls, task_name: str, uri_pm_path: str, creator: str, uri_pm_repo: str=None, pm_file_type: str=None,
                 pm_module: str=None, pm_handler: str=None, pm_kwargs: dict=None, default_save=None,
                 reset_templates: bool=None, template_path: str=None, template_module: str=None,
                 template_source_handler: str=None, template_persist_handler: str=None, align_connectors: bool=None,
                 default_save_intent: bool=None, default_intent_level: bool=None, order_next_available: bool=None,
                 default_replace_intent: bool=None, has_contract: bool=None) -> FeatureBuild:
        """ Class Factory Method to instantiates the components application. The Factory Method handles the
        instantiation of the Properties Manager, the Intent Model and the persistence of the uploaded properties.
        See class inline docs for an example method

         :param task_name: The reference name that uniquely identifies a task or subset of the property manager
         :param uri_pm_path: A URI that identifies the resource path for the property manager.
         :param creator: A user name for this task activity.
         :param uri_pm_repo: (optional) A repository URI to initially load the property manager but not save to.
         :param pm_file_type: (optional) defines a specific file type for the property manager
         :param pm_module: (optional) the module or package name where the handler can be found
         :param pm_handler: (optional) the handler for retrieving the resource
         :param pm_kwargs: (optional) a dictionary of kwargs to pass to the property manager
         :param default_save: (optional) if the configuration should be persisted. default to 'True'
         :param reset_templates: (optional) reset connector templates from environ variables. Default True
                                (see `report_environ()`)
         :param template_path: (optional) a template path to use if the environment variable does not exist
         :param template_module: (optional) a template module to use if the environment variable does not exist
         :param template_source_handler: (optional) a template source handler to use if no environment variable
         :param template_persist_handler: (optional) a template persist handler to use if no environment variable
         :param align_connectors: (optional) resets aligned connectors to the template. default Default True
         :param default_save_intent: (optional) The default action for saving intent in the property manager
         :param default_intent_level: (optional) the default level intent should be saved at
         :param order_next_available: (optional) if the default behaviour for the order should be next available order
         :param default_replace_intent: (optional) the default replace existing intent behaviour
         :param has_contract: (optional) indicates the instance should have a property manager domain contract
         :return: the initialised class instance
         """
        pm_file_type = pm_file_type if isinstance(pm_file_type, str) else 'parquet'
        pm_module = pm_module if isinstance(pm_module, str) else cls.DEFAULT_MODULE
        pm_handler = pm_handler if isinstance(pm_handler, str) else cls.DEFAULT_PERSIST_HANDLER
        _pm = FeatureBuildPropertyManager(task_name=task_name, creator=creator)
        _intent_model = FeatureBuildIntentModel(property_manager=_pm, default_save_intent=default_save_intent,
                                             default_intent_level=default_intent_level,
                                             order_next_available=order_next_available,
                                             default_replace_intent=default_replace_intent)
        super()._init_properties(property_manager=_pm, uri_pm_path=uri_pm_path, default_save=default_save,
                                 uri_pm_repo=uri_pm_repo, pm_file_type=pm_file_type, pm_module=pm_module,
                                 pm_handler=pm_handler, pm_kwargs=pm_kwargs, has_contract=has_contract)
        return cls(property_manager=_pm, intent_model=_intent_model, default_save=default_save,
                   reset_templates=reset_templates, template_path=template_path, template_module=template_module,
                   template_source_handler=template_source_handler, template_persist_handler=template_persist_handler,
                   align_connectors=align_connectors)

    @property
    def pm(self) -> FeatureBuildPropertyManager:
        return self._component_pm

    @property
    def intent_model(self) -> FeatureBuildIntentModel:
        return self._intent_model

    @property
    def tools(self) -> FeatureBuildIntentModel:
        return self._intent_model

    def run_component_pipeline(self, canonical: Any=None, intent_levels: [str, int, list]=None, run_book: str=None,
                               use_default: bool=None, seed: int=None, reset_changed: bool=None, has_changed: bool=None,
                               **kwargs):
        """runs the synthetic component pipeline. By passing an int value as the canonical will generate a synthetic
        file of that size

        :param canonical: (optional) to start the pipeline or a size of the synthetic build
        :param intent_levels: (optional) a single or list of intent levels to run
        :param run_book: (optional) a saved runbook to run
        :param use_default: (optional) if the default runbook should be used if it exists
        :param seed: (optional) a seed value for this run
        :param reset_changed: (optional) resets the has_changed boolean to True
        :param has_changed: (optional) tests if the underline canonical has changed since last load else error returned
        :param kwargs: any additional kwargs
        """
        use_default = use_default if isinstance(use_default, bool) else True
        if 'size' in kwargs.keys() and canonical is None:
            canonical = kwargs.pop('size')
        if canonical is None:
            canonical = self.load_source_canonical(reset_changed=reset_changed, has_changed=has_changed)
        if not isinstance(run_book, str) and use_default:
            if self.pm.has_run_book(book_name=self.pm.PRIMARY_RUN_BOOK):
                run_book = self.pm.PRIMARY_RUN_BOOK
        result = self.intent_model.run_intent_pipeline(canonical=canonical, intent_levels=intent_levels,
                                                       run_book=run_book, seed=seed, **kwargs)
        self.save_persist_canonical(result)
