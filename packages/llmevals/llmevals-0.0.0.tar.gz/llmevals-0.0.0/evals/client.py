"""Client for Twilix Evals
"""
import os
from .pipeline import Pipeline
from .api import Api
from .metric import Metric
from tqdm.auto import tqdm


class Evaluator(Api):
    def __init__(self, api_key: str = None, **kwargs):
        if api_key is None:
            api_key = os.environ["TWILIX_API_KEY"]
        self.api_key = api_key
        super().__init__(api_key=api_key, **kwargs)

    def add_ground_truth(self, query: str, expected_response: str, tags: list = None):
        """Add ground truth"""
        return self.post_request(
            endpoint="v1/pipeline/eval",
            body={"query": query, "expected_response": expected_response, "tags": tags},
        )

    def _get_ground_truths(self, take: int = 50, skip: int = 0):
        return self.get_request(
            endpoint="v1/pipeline/eval", params={"take": take, "skip": skip}
        )

    def _post_evaluation_result(
        self, evaluation_score: float, pipeline_id: str, test_id: str = None
    ):
        return self.post_request(
            endpoint="v1/pipeline/eval/run",
            body={
                "testId": test_id,
                "evaluationScore": evaluation_score,
                "pipelineGroupName": pipeline_id,
            },
        )

    def evaluate(self, pipeline: Pipeline, metric: Metric, test_id: str = None):
        #  {
        #     "created_at": "2023-08-10T09:28:44.782Z",
        #     "query": "Example",
        #     "expected_response": "Customer success response is here",
        #     "Tags": [
        #         "sample"
        #     ],
        #     "EvalRuns": []
        # },
        truths = self._get_ground_truths()
        for t in tqdm(truths["runs"]):
            result = pipeline.result_function(t["query"])
            expected_result = t["expected_response"]
            score = metric.measure(result, expected_result)
            result = self._post_evaluation_result(
                evaluation_score=score,
                pipeline_id=pipeline.pipeilne_id,
                test_id=t["id"],
            )
            print(result)
