from rc import prompt


def _prepare_message(stage, changes):
    changed_deps, changed_outs, changed_stage = changes
    if changed_deps and changed_outs:
        msg = "dependencies {deps} and outputs {outs} of {stage} changed."
    elif changed_deps:
        msg = "dependencies {deps} of {stage} changed."
    elif changed_outs:
        msg = "outputs {outs} of {stage} changed."
    else:
        msg = "{stage_changed}"

    msg += " Are you sure you want to get it?"

    kw = {
        "stage": stage,
        "deps": changed_deps,
        "outs": changed_outs,
        "stage_changed": changed_stage,
    }
    return msg.format_map(kw)

def prompt_to_get(stage, changes, force=False):
    from rc.stage.exceptions import StageCommitError

    if not (force or prompt.confirm(_prepare_message(stage, changes))):
        raise StageCommitError(
            f"unable to commit changed {stage}. Use `-f|--force` to force."
        )