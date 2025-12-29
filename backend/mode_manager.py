from ML.predictor import suggest_mode

def get_ml_recommendation(activity, current_mode):
    """
    Returns ML suggested mode or None.
    ML is disabled in EXAM mode.
    """
    if current_mode == "exam":
        return None

    return suggest_mode(activity)