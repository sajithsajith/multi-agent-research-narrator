from crewai import Task
from agents.agents import searcher_agent, summarizer_agent, tts_agent

search_task = Task(
    description=
        '''
         1. Search online for the topic: {topic}.
         2. Find all the relevant informations about the topic and return back
        ''',
    agent=searcher_agent,
    expected_output='Relevant informations focused on {topic}'
)

summarizer_task = Task(
    description=
        '''
         Summarize the provided text with words not exceeding 20.
        ''',
    agent=summarizer_agent,
    expected_output='A comprehensive summary within 20 words'
)


tts_task = Task(
    description='''
        1. Gather the summarized data.
        2. Convert the text to speech.
        3. Store the audio file in the provided directory: {file_path_tts}.
        ''',
    agent=tts_agent,
    expected_output='A success message of task completion'
)