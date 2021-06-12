import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.4, max_tokens=60)

# Add more examples for better results
gpt.add_example(Example("listen to music", "SongRecommend"))
gpt.add_example(Example("book a cab", "BookCab"))
gpt.add_example(Example("suggest movie recommendation", "MovieRecommend"))
gpt.add_example(Example("Schedule a meeting", "ScheduleMeeting"))
gpt.add_example(Example("Fetch food recipe", "RecipeRecommend"))

# Define UI configuration
config = UIConfig(
    description="Your Text",
    button_text="Run command",
    placeholder="Listen to music",
)

demo_web_app(gpt, config)