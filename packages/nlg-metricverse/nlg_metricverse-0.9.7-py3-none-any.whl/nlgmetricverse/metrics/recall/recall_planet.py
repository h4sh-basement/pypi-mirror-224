# coding=utf-8
# Copyright 2021 The HuggingFace evaluate Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Recall metric. The part of this file is adapted from HuggingFace's
evaluate package implementation of Recall metric. See
https://github.com/huggingface/evaluate/blob/master/metrics/recall/recall.py
"""

from collections import Counter
from typing import Callable

import evaluate
import numpy as np

from nlgmetricverse.collator import Collator
from nlgmetricverse.metrics._core import MetricForLanguageGeneration
from nlgmetricverse.utils.string import normalize_text

_CITATION = """\
@inproceedings{papineni2002bleu,
  title={Bleu: a method for automatic evaluation of machine translation},
  author={Papineni, Kishore and Roukos, Salim and Ward, Todd and Zhu, Wei-Jing},
  booktitle={Proceedings of the 40th annual meeting of the Association for Computational Linguistics},
  pages={311--318},
  year={2002}
}
"""

_DESCRIPTION = """\
This metric is derived from Modified Unigram Precision as a recall metric so that
it will compute across references and not across predictions unlike precision. The computation is similar, however,
we call this recall since there is no measure called "modified unigram recall".
Recall is the fraction of the common unigrams between the prediction
and the references among the reference tokens. It can be computed with:
Recall = # of matching tokens / # of reference tokens
"""

_KWARGS_DESCRIPTION = """\
Args:
    predictions: list of predictions to score. Each predictions
        should be a string with tokens separated by spaces.
    references: list of reference for each prediction. Each
        reference should be a string with tokens separated by spaces.
Returns:
    'score': Recall score.
Examples:

    >>> recall = nlgmetricverse.load_metric("recall")
    >>> predictions = [["the cat is on the mat", "There is cat playing on the mat"], ["Look! a wonderful day."]]
    >>> references = [
        ["the cat is playing on the mat.", "The cat plays on the mat."], 
        ["Today is a wonderful day", "The weather outside is wonderful."]
    ]
    >>> results = recall.compute(predictions=predictions, references=references)
    >>> print(results)
    {'recall': {'score': 0.7285714285714285}}
"""


@evaluate.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class RecallPlanet(MetricForLanguageGeneration):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=self._default_features,
            reference_urls=["https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html"],
        )

    def _tokenize(self, predictions: Collator, references: Collator):
        predictions = [normalize_text(p).split() for p in predictions]
        references = [normalize_text(r).split() for r in references]
        return predictions, references

    def _compute_single_pred_single_ref(
        self, predictions: Collator, references: Collator, reduce_fn: Callable = None, **kwargs
    ):
        """
        Compute the recall score for a single prediction and a single reference.
        Args:
            predictions (Collator): A Collator containing a single text sample for prediction.
            references (Collator): A Collator containing a single text sample for reference.
            reduce_fn (Callable, optional): A function to apply reduction to computed scores.
        """
        scores = []
        predictions, references = self._tokenize(predictions, references)
        for pred, ref in zip(predictions, references):
            if len(ref) == 0:
                scores.append(0)
                continue
            common = Counter(pred) & Counter(ref)  # Intersection count
            scores.append(sum(common.values()) / len(ref))
        avg_score = sum(scores) / len(scores)
        return {"score": avg_score}

    def _compute_single_pred_multi_ref(
        self, predictions: Collator, references: Collator, reduce_fn: Callable = None, **kwargs
    ):
        """
        Compute the recall score for a single prediction and multiple reference.
        Args:
            predictions (Collator): A Collator containing a single text sample for prediction.
            references (Collator): A Collator containing multiple text sample for reference.
            reduce_fn (Callable, optional): A function to apply reduction to computed scores.
        """
        scores = []
        for pred, refs in zip(predictions, references):
            pred_score = [
                self._compute_single_pred_single_ref(Collator([pred], keep=True), Collator([ref], keep=True))
                for ref in refs
            ]
            reduced_score = self._reduce_scores(pred_score, reduce_fn=reduce_fn)
            scores.append(reduced_score)

        return self._reduce_scores(scores, reduce_fn=np.mean)

    def _compute_multi_pred_multi_ref(
        self, predictions: Collator, references: Collator, reduce_fn: Callable = None, **kwargs
    ):
        """
        Compute the recall score for multiple prediction and multiple reference.
        Args:
            predictions (Collator): A Collator containing multiple text sample for prediction.
            references (Collator): A Collator containing multiple text sample for reference.
            reduce_fn (Callable, optional): A function to apply reduction to computed scores.
        """
        scores = []
        for preds, refs in zip(predictions, references):
            pred_scores = []
            for pred in preds:
                pred_score = self._compute_single_pred_multi_ref(
                    Collator([pred], keep=True), Collator([refs], keep=True), reduce_fn=reduce_fn
                )
                pred_scores.append(pred_score)
            reduced_score = self._reduce_scores(pred_scores, reduce_fn=reduce_fn)
            scores.append(reduced_score)

        return self._reduce_scores(scores, reduce_fn=np.mean)