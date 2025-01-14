from __future__ import absolute_import, division, print_function

import logging

from six.moves.urllib.parse import quote_plus

from locker.error import CliRunError
from locker.ls_resources.abstract import ListableAPIResource, CreateableAPIResource, UpdateableAPIResource, \
    DeletableAPIResource


class Secret(ListableAPIResource, CreateableAPIResource, UpdateableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "secret"

    @classmethod
    def get_secret(cls, key, environment_name=None, default_value=None,
                   access_key=None, api_base=None, api_version=None, **params):
        base = cls.class_cli()
        cli_ = '%s get --id "%s"' % (base, key)
        if environment_name:
            cli_ += ' --env "%s"' % environment_name
        instance = cls(None, access_key, **params)
        try:
            instance._call_and_refresh(
                cli_, access_key=access_key, api_base=api_base, api_version=api_version, params=params
            )
        except CliRunError as e:
            logging.warning(f"[!] CliRunError when get_secret of {key}. So return default value is {default_value}\n"
                            f"Traceback: {e}")
            return default_value
        try:
            return instance.data.value
        except AttributeError:
            return default_value

    @classmethod
    def modify(cls, **params):
        key = params.get("key")
        cli = '%s update --id "%s"' % (cls.class_cli(), key)

        environment_name = params.get("environment_name")
        if environment_name:
            cli += ' --env "%s"' % environment_name
            params.pop("environment_name", None)

        return cls._static_call(cli, params=params)

    @classmethod
    def create(cls, access_key=None, api_base=None, api_version=None, **params):
        cli = f"{cls.class_cli()} create"
        environment_name = params.get("environment_name")
        if not environment_name:
            params.update({"environment_name": None})
        return cls._static_call(
            cli,
            access_key,
            api_base=api_base,
            api_version=api_version,
            params=params,
        )
