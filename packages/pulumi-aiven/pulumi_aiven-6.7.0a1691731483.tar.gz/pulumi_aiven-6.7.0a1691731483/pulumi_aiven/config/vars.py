# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('aiven')


class _ExportableConfig(types.ModuleType):
    @property
    def api_token(self) -> Optional[str]:
        """
        Aiven Authentication Token
        """
        return __config__.get('apiToken')

