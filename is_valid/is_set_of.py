from .explanation import Explanation
from .is_iterable_of import is_iterable_of
from .is_set import is_set


class is_set_of(is_iterable_of):

    prerequisites = [is_set]

    def _evaluate_explain(self, data):
        data = list(data)
        explanation = super()._evaluate_explain(data)
        return Explanation(
            explanation.valid, explanation.code, explanation.message,
            {data[i]: e for i, e in explanation.details.items()},
        )