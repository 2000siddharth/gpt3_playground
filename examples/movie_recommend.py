import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=60)

gpt.add_example(
    Example(
        "The Godfather",
        "Crime, drama, The Godfather II, The Sopranos, Goodfellas, Peaky Blinders, The Departed",
    )
)
gpt.add_example(
    Example(
        "Friends",
        "Comedy, Sitcom, The Big Bang Theory, How I met your mother, Seinfield, Two and a half men, Joey",
    )
)
gpt.add_example(
    Example(
        "Titanic",
        "Romance, Tragedy, Leonardo Di Caprio, The Great Gatsby, The Revenant, Romeo and Juliet, A walk to remember, Forrest Gump",
    )
)
gpt.add_example(
    Example(
        "Inception",
        "Sci-Fi, Action, Cristopher Nolan, The Prestige, The Matrix, Memento, Limitless, Oblivion, Coherence",
    )
)
gpt.add_example(
    Example(
        "Interstellar",
        "Sci-Fi, Adventure, Space, Cristopher Nolan,The Martian, Apollo 13, Gravity, Arrival, Passengers, Firefly",
    )
)
gpt.add_example(
    Example(
        "Breaking Bad",
        "Crime, Drama, Thriller, Better Call Saul, Ozark, Prison Break, Power, Peaky Blinders, Bad Blood",
    )
)
gpt.add_example(
    Example(
        "Toy Story",
        "kids, Animation, Friendship, Monsters Inc, Toy Story 3, Up, Finding Nemo, The Lego Movie, Shrek",
    )
)
gpt.add_example(
    Example(
        "The Avengers",
        "Sci-fi, Adventure, Thriller, Iron Man 3, Thor, The Winter Soldier, The Avengers Infinity War, The Avengers Endgame, The Incredible Hulk, Spiderman Homecoming",
    )
)
gpt.add_example(
    Example(
        "The Notebook",
        "Love, Drama,  Romance, The Fault in our stars, The Last Song, A walk to remember, Keith, Blue Valentine",
    )
)


# Define UI configuration
config = UIConfig(
    description="Movie Recommendation",
    button_text="Return movies",
    placeholder="Titanic",
)

demo_web_app(gpt, config)
