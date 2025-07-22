from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopment2():
    """Course Creation and Review Crew (No Ingest Agent)"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def content_structurer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_structurer'], 
            verbose=True,
            human_input=True
        )

    @agent
    def objective_generator(self) -> Agent:
        return Agent(config=self.agents_config['objective_generator'], verbose=True, human_input=True)

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(config=self.agents_config['quiz_generator'], verbose=True, human_input=True)

    @agent
    def quiz_composer(self) -> Agent:
        return Agent(config=self.agents_config['quiz_composer'], verbose=True, human_input=True)

    # @agent
    # def course_reviewer(self) -> Agent:
    #     return Agent(config=self.agents_config['course_reviewer'], verbose=True)

    # @agent
    # def quiz_auditor(self) -> Agent:
    #     return Agent(config=self.agents_config['quiz_auditor'], verbose=True)

    # @agent
    # def content_updater(self) -> Agent:
    #     return Agent(config=self.agents_config['content_updater'], verbose=True)

    @task
    def structure_course(self) -> Task:
        return Task(
            config=self.tasks_config['structure_course'],
            human_input=True
        )

    @task
    def generate_objectives(self) -> Task:
        return Task(config=self.tasks_config['generate_objectives'], human_input=True)

    @task
    def generate_quiz(self) -> Task:
        return Task(config=self.tasks_config['generate_quiz'], human_input=True)

    @task
    def compose_quiz_sets(self) -> Task:
        return Task(config=self.tasks_config['compose_quiz_sets'], human_input=True)
    
    # @task
    # def review_course(self) -> Task:
    #     return Task(config=self.tasks_config['review_course'])

    # @task
    # def audit_quizzes(self) -> Task:
    #     return Task(config=self.tasks_config['audit_quizzes'])

    # @task
    # def update_course_content(self) -> Task:
    #     return Task(config=self.tasks_config['update_course_content'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
