"""Fixtures for the housekeeper tests."""
from pathlib import Path
from typing import List

import datetime

import pytest

from cg.apps.housekeeper.hk import HousekeeperAPI
from housekeeper.store.models import Bundle

from tests.mocks.hk_mock import MockHousekeeperAPI


@pytest.fixture(name="hk_config")
def fixture_hk_config(root_path: Path) -> dict:
    """Return a dictionary with housekeeper api configs for testing."""
    return {"housekeeper": {"database": "sqlite:///:memory:", "root": root_path.as_posix()}}


@pytest.fixture(scope="function", name="housekeeper_api")
def fixture_housekeeper_api(hk_config):
    """Setup Housekeeper store."""
    _api = HousekeeperAPI(hk_config)
    _api.initialise_db()
    yield _api
    _api.destroy_db()


@pytest.fixture(name="new_bundle_name")
def fixture_new_bundle_name() -> str:
    """Return a bundle name that does not exist in the database."""
    return "new_name"


@pytest.fixture(name="minimal_bundle_obj")
def fixture_minimal_bundle_obj(
    timestamp: datetime.datetime, case_id: str, housekeeper_api: MockHousekeeperAPI
) -> Bundle:
    """Return a bundle object with minimal information (name and created_at)."""
    return housekeeper_api.new_bundle(name=case_id, created_at=timestamp)


@pytest.fixture(name="hk_tag")
def fixture_hk_tag() -> str:
    """Return a Housekeeper tag."""
    return "bed"


@pytest.fixture(name="tags")
def fixture_tags() -> List[str]:
    """Return a list of Housekeeper tags."""
    return ["bed"]


@pytest.fixture(name="not_existing_hk_tag")
def fixture_not_existing_hk_tag() -> str:
    """Return a non existing Housekeeper tag."""
    return "this_tag_should_not_exist_in_database"
