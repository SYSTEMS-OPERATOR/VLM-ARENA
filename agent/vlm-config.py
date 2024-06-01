import dotenv

dotenv.load_dotenv()

MODELS = {
    "OPENAI": {
        "openai:gpt-4-0125-preview",
        "openai:gpt-4o",
        # "openai:gpt-3.5-turbo-0125", # not a vlm
        # "openai:gpt-3.5-turbo-instruct", # not a chat model
    },
    "MISTRAL": {
        # "mistral:mistral-small-latest", # not a vlm
        # "mistral:mistral-medium-latest", # not a vlm
        # "mistral:mistral-large-latest", # not a vlm
        "groq:mistral-8x6b-32768", # probably not a vlm ?
    },
    "GROQ": {
      "groq:gemma-7b-it" # yeah.. not a VLM; can we get some GROQ VLM action here?
    },
    "ANTHROPIC": {"anthropic:claude-3-haiku-20240307"},
# Need a hook for Gemini
}

MOVES = {
    "No-Move": 0,
    "Left": 1,
    "Left+Up": 2,
    "Up+Left": 2,
    "Up": 3,
    "Up+Right": 4,
    "Right+Up": 4,
    "Right": 5,
    "Right+Down": 6,
    "Down+Right": 6,
    "Down": 7,
    "Down+Left": 8,
    "Left+Down": 8,
    "Low Punch": 9,
    "Medium Punch": 10,
    "High Punch": 11,
    "Low Kick": 12,
    "Medium Kick": 13,
    "High Kick": 14,
    "Low Punch+Low Kick": 15,
    "Medium Punch+Medium Kick": 16,
    "High Punch+High Kick": 17,
}

MOVES_WITH_LOWER = {
    **MOVES,
    **{key.lower(): value for key, value in MOVES.items()},
}

COMBOS = {
    "Kikoken": {"right": [6, 5, 11], "left": [8, 1, 11]},
    "Spinning Bird Kick": {
        "right": [7, 6, 5, 4, 3, 13],
        "left": [7, 8, 1, 2, 3, 13],
    },
    "Hyakuretsukyaku": {
        "right": [9, 9, 9, 9, 9],
        "left": [9, 9, 9, 9, 9],
    },
}

SPECIAL_MOVES = {
    "EX-Kikoken": {"right": [6, 5, 11, 11], "left": [8, 1, 11, 11]},
    "EX-Spinning Bird Kick": {
        "right": [7, 6, 5, 4, 3, 13, 13],
        "left": [7, 8, 1, 2, 3, 13, 13],
    },
    "EX-Hyakuretsukyaku": {
        "right": [9, 9, 9, 9, 9, 9],
        "left": [9, 9, 9, 9, 9, 9],
    },
}

META_INSTRUCTIONS = {
    "Move Closer": {"right": [5, 5, 5, 5], "left": [1, 1, 1, 1]},
    "Move Away": {"right": [1, 1, 1, 1], "left": [5, 5, 5, 5]},
    "Kikoken": COMBOS["Kikoken"],
    "Spinning Bird Kick": COMBOS["Spinning Bird Kick"],
    "Hyakuretsukyaku": COMBOS["Hyakuretsukyaku"],
    "EX-Kikoken": SPECIAL_MOVES["EX-Kikoken"],
    "EX-Spinning Bird Kick": SPECIAL_MOVES["EX-Spinning Bird Kick"],
    "EX-Hyakuretsukyaku": SPECIAL_MOVES["EX-Hyakuretsukyaku"],
    **{
        move_name: {"right": [move_nb, 0], "left": [move_nb, 0]}
        for move_name, move_nb in MOVES.items()
        if "Punch" in move_name or "Kick" in move_name
    },
    "Jump Closer": {"right": [4, 4, 4, 4], "left": [2, 2, 2, 2]},
    "Jump Away": {"right": [2, 2, 2, 2], "left": [4, 4, 4, 4]},
}

META_INSTRUCTIONS_WITH_LOWER = {
    **META_INSTRUCTIONS,
    **{key.lower(): value for key, value in META_INSTRUCTIONS.items()},
    "lower": {"right": [12, 0], "left": [12, 0]},
    "medium": {"right": [13, 0], "left": [13, 0]},
    "med": {"right": [13, 0], "left": [13, 0]},
    "high": {"right": [14, 0], "left": [14, 0]},
}

INDEX_TO_MOVE = {v: k for k, v in MOVES.items()}

X_SIZE = 384
Y_SIZE = 224

REAL_MOVE_LIST = [
    "No-Move",
    "Left",
    "Left+Up",
    "Up",
    "Right",
    "Right+Down",
    "Down",
    "Down+Left",
    "Low Punch",
    "Medium Punch",
    "High Punch",
    "Low Kick",
    "Medium Kick",
    "High Kick",
    "Low Punch+Low Kick",
    "Medium Punch+Medium Kick",
    "High Punch+High Kick",
]

NB_FRAME_WAIT = 1
