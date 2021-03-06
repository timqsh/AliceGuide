STATE_REQUEST_KEY = "session"
STATE_RESPONSE_KEY = "session_state"
USERSTATE_RESPONSE_KEY = "user_state_update"

# region State of dialog

QUESTION_TYPE = "question_type"
PREVIOUS_SCENE = "previous"
QUESTION_ID = "question_id"
ASKED_QUESTIONS = "asked_questions"
TOUR_ID = "tour_id"
TOUR_LEVEL = "tour_level"
END_TOUR = "end_of_tour"
HAVE_MORE_QUESTIONS = "have_more_questions"
LOCATION = "location"  # 58.52113680728278, 31.27517020919651 (координаты памятника)

# endregion

MUST_BE_SAVE = {QUESTION_TYPE, PREVIOUS_SCENE, QUESTION_ID}
PERMANENT_VALUES = {ASKED_QUESTIONS}
USER_STATE = {TOUR_ID, TOUR_LEVEL}  # Для очистки данных
