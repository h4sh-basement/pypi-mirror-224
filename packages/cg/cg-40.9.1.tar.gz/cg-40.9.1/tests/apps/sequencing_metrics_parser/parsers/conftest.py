from typing import Dict
import pytest

from cg.apps.sequencing_metrics_parser.models.bcl2fastq_metrics import (
    ConversionResult,
    DemuxResult,
    IndexMetric,
    ReadMetric,
)


@pytest.fixture
def valid_bcl2fastq_metrics_data() -> Dict:
    """Example structure of a valid stats.json file containing sequecing metrics generated by bcl2fastq."""
    return {
        "Flowcell": "AB1",
        "RunNumber": 1,
        "RunId": "RUN1",
        "ReadInfosForLanes": [
            {
                "LaneNumber": 1,
            }
        ],
        "ConversionResults": [
            {
                "LaneNumber": 1,
                "Yield": 1000,
                "DemuxResults": [
                    {
                        "SampleId": "S1",
                        "SampleName": "Sample1",
                        "IndexMetrics": [
                            {
                                "IndexSequence": "ATGC",
                                "MismatchCounts": {"0": 24470341, "1": 5093729},
                            }
                        ],
                        "NumberReads": 1,
                        "Yield": 100,
                        "ReadMetrics": [
                            {"ReadNumber": 1, "Yield": 100, "YieldQ30": 90, "QualityScoreSum": 100}
                        ],
                    }
                ],
            }
        ],
    }


@pytest.fixture
def conversion_result() -> ConversionResult:
    return ConversionResult(
        LaneNumber=1,
        Yield=1000,
        DemuxResults=[
            DemuxResult(
                SampleId="S1",
                SampleName="Sample1",
                IndexMetrics=[
                    IndexMetric(IndexSequence="ATGC", MismatchCounts={"0": 24470341, "1": 5093729})
                ],
                NumberReads=1,
                Yield=100,
                ReadMetrics=[ReadMetric(ReadNumber=1, Yield=100, YieldQ30=90, QualityScoreSum=100)],
            )
        ],
    )
