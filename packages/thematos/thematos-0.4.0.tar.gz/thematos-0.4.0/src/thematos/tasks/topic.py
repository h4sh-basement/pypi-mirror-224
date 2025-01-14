import itertools
import os
import random
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from hyfi import HyFI
from hyfi.task import BatchTaskConfig
from hyfi.utils.contexts import elapsed_timer
from tqdm.auto import tqdm

from thematos.datasets.corpus import Corpus
from thematos.models.lda import LdaModel
from thematos.models.prior import WordPrior
from thematos.models.types import IDF, ONE, PMI, ModelSummary

logger = HyFI.getLogger(__name__)


class TopicTask(BatchTaskConfig):
    _config_group_ = "/task"
    _config_name_ = "topic"

    model_name: str = "TopicModel"

    model: LdaModel = LdaModel()

    num_workers: int = 0
    ngram: int = None
    files: dict = None
    verbose: bool = False

    _summaries_: List[ModelSummary] = []
    active_model_id: Optional[str] = None

    models = {}

    @property
    def summary_file(self) -> Path:
        summary_file = f"{self.model_name}_summaries.csv"
        return self.output_dir / summary_file

    @property
    def summaries(self) -> List[ModelSummary]:
        if self._summaries_:
            return self._summaries_
        summaries = []
        if HyFI.is_file(self.summary_file):
            data = HyFI.load_dataframe(self.summary_file, index_col=0)
            summaries.extend(ModelSummary(*row[1:]) for row in data.itertuples())
        self._summaries_ = summaries
        return summaries
