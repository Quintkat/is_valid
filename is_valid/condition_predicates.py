def is_any(*predicates):
    def is_valid(data, explain=False):
        if not explain:
            return any(predicate(data) for predicate in predicates)
        reasons, errors = [], []
        for i, predicate in enumerate(predicates):
            valid, explanation = predicate(data, explain=True)
            (reasons if valid else errors).append(explanation)
        return (True, reasons) if reasons else (False, errors)
    return is_valid


def is_all(*predicates):
    def is_valid(data, explain=False):
        if not explain:
            return all(predicate(data) for predicate in predicates)
        reasons, errors = [], []
        for i, predicate in enumerate(predicates):
            valid, explanation = predicate(data, explain=True)
            (reasons if valid else errors).append(explanation)
        return (True, reasons) if not errors else (False, errors)
    return is_valid


def is_if(cond, pred_if, pred_else=lambda _, explain=False: (
    True, 'data does not match the condition'
) if explain else True):
    def is_valid(data, explain=True):
        return (pred_if if cond(data) else pred_else)(data, explain=explain)
    return is_valid


def is_cond(*conds):
    def is_valid(_, explain=False):
        return (
            False, 'data matches none of the conditions'
        ) if explain else False
    for cond, predicate in reversed(conds):
        is_valid = is_if(cond, predicate, is_valid)
    return is_valid
