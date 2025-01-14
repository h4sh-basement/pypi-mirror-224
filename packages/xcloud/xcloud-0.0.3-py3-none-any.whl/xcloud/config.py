from pathlib import Path
import tempfile
import os
from dotenv import load_dotenv, find_dotenv

# IMPORTANT: dont import logger here (circular import)

env_path = find_dotenv()
load_dotenv(env_path)


class Config:
    DEBUG = os.getenv("DEBUG", "false").lower() in ('true', '1', 't')
    ACCELERATION_BASE_URL_X_BACKEND = os.environ.get(
        "ACCELERATION_BASE_URL_X_BACKEND", 
        "https://xcloud-api.stochastic.ai/acceleron/backend"
    )
    EXECUTION_BASE_URL_X_BACKEND = os.environ.get(
        "EXECUTION_BASE_URL_X_BACKEND", 
        "https://xcloud-api.stochastic.ai/executor/backend"
    )
    DEPLOYMENTS_BASE_URL_X_BACKEND = os.environ.get(
        "DEPLOYMENTS_BASE_URL_X_BACKEND", 
        "https://xcloud-api.stochastic.ai/inference/backend"
    )
    NOTEBOOKS_BASE_URL_X_BACKEND = os.environ.get(
        "NOTEBOOKS_BASE_URL_X_BACKEND", 
        "https://xcloud-api.stochastic.ai/notebook/backend"
    )
    PANEL_DOMAIN = "https://xcloud.stochastic.ai"
    AUTH_BASE_URL_X_BACKEND = os.environ.get(
        "AUTH_BASE_URL_X_BACKEND", 
        "https://xcloud-api.stochastic.ai/auth/backend"
    )
    XCLOUD_CONFIG_PATH: Path = Path.home() / ".xcloud" / "config"
    XCLOUD_ASSETS: Path = Path.home() / ".xcloud" / "assets"
    DEFAULT_FT_DOCKER_IMAGE = os.environ.get(
        "DEFAULT_FT_DOCKER_IMAGE", 
        "us-central1-docker.pkg.dev/stochastic-x/xcloud-public/inference:ft_v0.0.1"
    )
    DEFAULT_VLLM_DOCKER_IMAGE = os.environ.get(
        "DEFAULT_VLLM_DOCKER_IMAGE", 
        "us-central1-docker.pkg.dev/stochastic-x/xcloud-public/inference:vllm_v0.0.1"
    )