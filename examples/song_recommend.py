import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=60)

gpt.add_example(
    Example(
        "Rock",
        "Come Together, House of Rising Sun, Paradise City, Hammer of God, Hotel California, Bohemian Rhapsody",
    )
)
gpt.add_example(
    Example(
        "Romantic",
        "Perfect, A sky full of stars, I like me better, All of me, Thinking out loud, Hey Jude, A thousand years",
    )
)
gpt.add_example(
    Example(
        "Chill",
        "Cheap Thrills, Memories, Little things, At my worst, This city, Before you go",
    )
)
gpt.add_example(
    Example(
        "Sad",
        "enough for you, Falling, Train wreck, learn to let go, Another love, Humdard, Shayad",
    )
)
gpt.add_example(
    Example(
        "Happy",
        "Closer, Something just like this, Uptown girl, Fireflies, The scientist",
    )
)
gpt.add_example(
    Example(
        "Motivational",
        "It's my life, Hall of fame, I want to break free, Let it go, Wavin Flag, Don't give up",
    )
)
gpt.add_example(
    Example(
        "Bollywood",
        "Tum hi ho, Tum se hi, Soch na sake, Sab tera, Humsafar, Suit suit, Hoor",
    )
)


# Define UI configuration
config = UIConfig(
    description="Enter your mood or Genre",
    button_text="Return songs",
    placeholder="Rock",
)

demo_web_app(gpt, config)
