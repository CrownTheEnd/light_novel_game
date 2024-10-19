characters = {
    "Acheron": {
        "dialogue": {
            1: "Hello, traveler!",
            2: "Are you ready for the adventure?",
            3: "Let's begin!"
        },
        "dialogue_index": 1,  # Store current dialogue index for each character
        "image_file": "Images\characters\Acheron_Render.png"
    },
    "Nyx": {
        "dialogue": {
            1: "Greetings, mortal.",
            2: "What brings you here?",
            3: "Farewell."
        },
        "dialogue_index": 1
    }
}

Scenes = {
    1: {
        "dialogue": {
            1: [
                "Acheron", 
                "Hello, traveler!",
                "multi",
                ],
            "1":[[
                "Trailblazer", 
                  "Hello!",
                  "Acheron",
                  "Oh, so well mannered."
                  
                ],
                [
                "Trailblazer", 
                  "You suck Acheron!",
                  "Acheron",
                  "Oh okay, damn, bitch."
                ],
                [
                "Trailblazer", 
                  "Give me a free 5 star!",
                  "Acheron",
                  "Ungrateful little.."
                ]],
            2: ["Silverwolf", "Are you ready for the adventure?"],
            3: ["Acheron", "Let's begin!"]
        },
        "dialogue_index": 1,  # Store current dialogue index for each character
        "background": "Images\menu_item_background.png",
        "bgm_file": "audio\music\menu_theme.wav",
        "characters": {
            "Acheron": "Images\characters\Acheron_Render.png",
            "Silverwolf": "",
        }
    },
    "Nyx": {
        "dialogue": {
            1: "Greetings, mortal.",
            2: "What brings you here?",
            3: "Farewell."
        },
        "dialogue_index": 1
    }
}

