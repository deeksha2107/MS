import sys
from dotenv import load_dotenv
load_dotenv()
from recipe_crew.crew import RecipeGenerator 
def run():
    inputs = {"topic": "Avakai Pachadi"}  
    result = RecipeGenerator().crew().kickoff(inputs=inputs)
    print(result)

if __name__ == '__main__':
    run()