from pathlib import Path

import pytest
from cg.apps.slurm.slurm_api import SlurmAPI
from cg.models.slurm.sbatch import Sbatch
from tests.mocks.process_mock import ProcessMock


@pytest.fixture(name="sbatch_parameters")
def fixture_sbatch_parameters(email_adress: str, slurm_account: str) -> Sbatch:
    """Return sbatch parameters."""
    config = {
        "job_name": "test",
        "account": slurm_account,
        "number_tasks": 3,
        "memory": 10,
        "log_dir": "path/to/dir",
        "email": email_adress,
        "hours": 2,
        "commands": "genmod",
    }
    return Sbatch.parse_obj(config)


@pytest.fixture(name="sbatch_content")
def fixture_sbatch_content(sbatch_parameters: Sbatch) -> str:
    """Return sbatch content."""
    api = SlurmAPI()
    return api.generate_sbatch_content(sbatch_parameters=sbatch_parameters)


@pytest.fixture(name="slurm_api")
def fixture_slurm_api(sbatch_process: ProcessMock) -> SlurmAPI:
    """Return a slurm API with the process mocked."""
    api = SlurmAPI()
    api.process = sbatch_process
    return api


@pytest.fixture(name="sbatch_path")
def fixture_sbatch_path(project_dir: Path) -> Path:
    """Return sbatch path."""
    return Path(project_dir, "sbatch_file.sh")
