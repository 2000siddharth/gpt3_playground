import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.4, max_tokens=60)

gpt.add_example(
    Example(
        "Fetch unique values of DEPARTMENT from Worker table.",
        "Select distinct DEPARTMENT from Worker;",
    )
)
gpt.add_example(
    Example(
        "Print the first three characters of FIRST_NAME from Worker table.",
        "Select substring(FIRST_NAME,1,3) from Worker;",
    )
)
gpt.add_example(
    Example(
        "Find the position of the alphabet ('a') in the first name column 'Amitabh' from Worker table.",
        "Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'Amitabh';",
    )
)
gpt.add_example(
    Example(
        "Print the FIRST_NAME from Worker table after replacing 'a' with 'A'.",
        "Select CONCAT(FIRST_NAME, ' ', LAST_NAME) AS 'COMPLETE_NAME' from Worker;",
    )
)
gpt.add_example(
    Example(
        "Display the second highest salary from the Worker table.",
        "Select max(Salary) from Worker where Salary not in (Select max(Salary) from Worker);",
    )
)
gpt.add_example(
    Example(
        "Display the highest salary from the Worker table.",
        "Select max(Salary) from Worker;",
    )
)
gpt.add_example(
    Example(
        "Fetch the count of employees working in the department Admin.",
        "SELECT COUNT(*) FROM worker WHERE DEPARTMENT = 'Admin';",
    )
)
gpt.add_example(
    Example(
        "Get all details of the Workers whose SALARY lies between 100000 and 500000.",
        "Select * from Worker where SALARY between 100000 and 500000;",
    )
)
gpt.add_example(
    Example("Get Salary details of the Workers", "Select Salary from Worker")
)


# Define UI configuration
config = UIConfig(
    description="Query to be created in plain text",
    button_text="Return Query",
    placeholder="Get Salary details of the Workers",
)

demo_web_app(gpt, config)
