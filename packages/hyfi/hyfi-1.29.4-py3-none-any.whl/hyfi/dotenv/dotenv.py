"""
Configuration class for environment variables in HyFI.
"""
from typing import Optional, Union

from hyfi.composer import BaseSettings, Field, SecretStr
from hyfi.utils.logging import LOGGING

logger = LOGGING.getLogger(__name__)


class DotEnvConfig(BaseSettings):
    """
    Configuration class for environment variables in HyFI.

    Attributes:
        _config_name_: str: Name of the configuration.
        DOTENV_FILENAME: Optional[str]: Name of the dotenv file.
        DOTENV_DIR: Optional[str]: Path to the dotenv file.
        DOTENV_FILE: Optional[str]: Full path to the dotenv file.
        HYFI_RESOURCE_DIR: Optional[str]: Path to the resource directory.
        HYFI_GLOBAL_ROOT: Optional[str]: Path to the global root directory.
        HYFI_GLOBAL_WORKSPACE_NAME: Optional[str]: Name of the global workspace.
        HYFI_PROJECT_NAME: Optional[str]: Name of the project.
        HYFI_PROJECT_DESC: Optional[str]: Description of the project.
        HYFI_PROJECT_ROOT: Optional[str]: Path to the project root directory.
        HYFI_PROJECT_WORKSPACE_NAME: Optional[str]: Name of the project workspace.
        HYFI_LOG_LEVEL: Optional[str]: Log level for HyFI.
        HYFI_VERBOSE: Optional[Union[bool, str, int]]: Verbosity level for HyFI.
        HYFI_NUM_WORKERS: Optional[int]: Number of workers for HyFI.
        CACHED_PATH_CACHE_ROOT: Optional[str]: Path to the cached path cache root.
        CUDA_DEVICE_ORDER: Optional[str]: CUDA device order.
        CUDA_VISIBLE_DEVICES: Optional[str]: CUDA visible devices.
        WANDB_PROJECT: Optional[str]: Name of the Weights & Biases project.
        WANDB_DISABLED: Optional[str]: Whether Weights & Biases is disabled.
        WANDB_DIR: Optional[str]: Path to the Weights & Biases directory.
        WANDB_NOTEBOOK_NAME: Optional[str]: Name of the Weights & Biases notebook.
        WANDB_SILENT: Optional[Union[bool, str]]: Whether Weights & Biases is silent.
        LABEL_STUDIO_SERVER: Optional[str]: URL of the Label Studio server.
        KMP_DUPLICATE_LIB_OK: Optional[str]: Whether to allow duplicate libraries for Intel MKL.
        TOKENIZERS_PARALLELISM: Optional[Union[bool, str]]: Whether tokenizers are parallelized.
        WANDB_API_KEY: Optional[SecretStr]: Weights & Biases API key.
        HUGGING_FACE_HUB_TOKEN: Optional[SecretStr]: Hugging Face Hub token.
        OPENAI_API_KEY: Optional[SecretStr]: OpenAI API key.
        ECOS_API_KEY: Optional[SecretStr]: ECOS API key.
        FRED_API_KEY: Optional[SecretStr]: FRED API key.
        NASDAQ_API_KEY: Optional[SecretStr]: NASDAQ API key.
        HF_USER_ACCESS_TOKEN: Optional[SecretStr]: Hugging Face user access token.
        LABEL_STUDIO_USER_TOKEN: Optional[SecretStr]: Label Studio user token.
        model_config: SettingsConfigDict: Configuration dictionary for the model.
    """

    """Environment variables for HyFI"""

    _config_name_: str = "__init__"
    _config_group_: str = "/dotenv"

    # Internal
    HYFI_RESOURCE_DIR: Optional[str] = None
    HYFI_GLOBAL_ROOT: Optional[str] = None
    HYFI_GLOBAL_WORKSPACE_NAME: Optional[str] = ".hyfi"
    HYFI_PROJECT_NAME: Optional[str] = None
    HYFI_PROJECT_DESC: Optional[str] = None
    HYFI_PROJECT_ROOT: Optional[str] = None
    HYFI_PROJECT_WORKSPACE_NAME: Optional[str] = "workspace"
    HYFI_LOG_LEVEL: Optional[str] = "WARNING"
    HYFI_VERBOSE: Optional[Union[bool, str, int]] = False
    HYFI_NUM_WORKERS: Optional[int] = 1
    CACHED_PATH_CACHE_ROOT: Optional[str] = None
    # For other packages
    CUDA_DEVICE_ORDER: Optional[str] = "PCI_BUS_ID"
    CUDA_VISIBLE_DEVICES: Optional[Union[str, int]] = None
    WANDB_PROJECT: Optional[str] = None
    WANDB_DISABLED: Optional[Union[bool, str]] = None
    WANDB_DIR: Optional[str] = None
    WANDB_NOTEBOOK_NAME: Optional[str] = None
    WANDB_SILENT: Optional[Union[bool, str]] = None
    LABEL_STUDIO_SERVER: Optional[str] = None
    KMP_DUPLICATE_LIB_OK: Optional[str] = "True"
    TOKENIZERS_PARALLELISM: Optional[Union[bool, str]] = False
    # API Keys and Tokens
    WANDB_API_KEY: Optional[SecretStr] = Field(exclude=True, default="")
    HUGGING_FACE_HUB_TOKEN: Optional[SecretStr] = Field(exclude=True, default="")
    OPENAI_API_KEY: Optional[SecretStr] = Field(exclude=True, default="")
    ECOS_API_KEY: Optional[SecretStr] = Field(exclude=True, default="")
    FRED_API_KEY: Optional[SecretStr] = Field(exclude=True, default="")
    NASDAQ_API_KEY: Optional[SecretStr] = Field(exclude=True, default="")
    HF_USER_ACCESS_TOKEN: Optional[SecretStr] = Field(exclude=True, default="")
    LABEL_STUDIO_USER_TOKEN: Optional[SecretStr] = Field(exclude=True, default="")
