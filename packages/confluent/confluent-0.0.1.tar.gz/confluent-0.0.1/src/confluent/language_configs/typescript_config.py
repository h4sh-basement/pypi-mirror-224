from typing import List

from ..generators.typescript_generator import TypescriptGenerator

from ..base.language_config_naming_conventions import LanguageConfigNamingConventions
from ..base.language_config_base import LanguageConfigBase
from ..base.language_type import LanguageType
from ..base.property import Property


class TypescriptConfig(LanguageConfigBase):
    """
    TypeScript specific config. For more information about the config methods, refer to LanguageConfigBase.
    """

    def __init__(
        self,
        config_name: str,
        properties: List[Property],
        indent: int = None,
        naming_conventions: LanguageConfigNamingConventions = None,
        additional_props = {},
    ):
        super().__init__(
            config_name,
            LanguageType.TYPESCRIPT,
            'ts',
            TypescriptGenerator,
            properties,
            indent,
            naming_conventions,
            additional_props,
        )
