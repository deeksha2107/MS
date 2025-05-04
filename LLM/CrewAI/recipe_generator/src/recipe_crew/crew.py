from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

  
@CrewBase
class RecipeGenerator():
    agents: List[BaseAgent]
    tasks: List[Task]
    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs 
    
    '''@after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result '''

    @agent
    def recipe_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['recipe_researcher'], 
            verbose=True
            )
    @agent
    def recipe_writer(self) -> Agent:
        return Agent(
        config=self.agents_config['recipe_writer'], 
        verbose=True
        )
    
    @task
    def recipe_research_task(self) -> Task:
        return Task(
        config=self.tasks_config['recipe_research_task'], 
        )
    @task
    def recipe_writer_task(self) -> Task:
        return Task(
        config=self.tasks_config['recipe_writer_task'], 
        output_file='output/recipe.pdf' 
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True,
        )
    