import pytest
from sqlalchemy import update

from cg.apps.cgstats.db import models as stats_models
from cg.apps.cgstats.stats import StatsAPI
from cg.models.cg_config import CGConfig
from cg.store import Store


from tests.store.api.conftest import (
    fixture_re_sequenced_sample_store,
    fixture_store_failing_sequencing_qc,
)

from tests.apps.cgstats.conftest import fixture_nipt_stats_api
from tests.store.api.conftest import fixture_re_sequenced_sample_store
from cg.store.models import Application


@pytest.fixture(name="nipt_upload_api_context")
def fixture_nipt_upload_api_context(
    cg_context: CGConfig, re_sequenced_sample_store: Store
) -> CGConfig:
    cg_context.status_db_ = re_sequenced_sample_store

    return cg_context


@pytest.fixture(name="nipt_upload_api_failed_fc_context")
def fixture_nipt_upload_api_failed_fc_context(
    nipt_upload_api_context: CGConfig, sample_id: str, store_failing_sequencing_qc: Store
) -> CGConfig:
    nipt_upload_api_failed_fc_context: CGConfig = nipt_upload_api_context
    nipt_upload_api_failed_fc_context.status_db_ = store_failing_sequencing_qc
    status_db = nipt_upload_api_context.status_db

    application = status_db.get_sample_by_internal_id(
        internal_id=sample_id
    ).application_version.application
    status_db.session.execute(
        update(Application).where(Application.id == application.id).values({"target_reads": 20})
    )

    return nipt_upload_api_failed_fc_context
