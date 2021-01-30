STATE_REQUEST_KEY = "session"
STATE_RESPONSE_KEY = "session_state"

# region State of dialog

QUESTION_TYPE = "question_type"
PREVIOUS_SCENE = "previous"
QUESTION_ID = "question_id"
ASKED_QUESTIONS = "asked_questions"
TOUR_ID = "tour_id"
TOUR_LEVEL = "tour_level"
BREAK = "break"

# endregion

MUST_BE_SAVE = {QUESTION_TYPE, PREVIOUS_SCENE, QUESTION_ID}
PERMANENT_VALUES = {ASKED_QUESTIONS, TOUR_ID, TOUR_LEVEL}
