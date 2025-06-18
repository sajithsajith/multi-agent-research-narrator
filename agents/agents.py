from crewai import Agent
import soundfile as sf

from tools.agent_tools import tts, search_tool
from models.models import load_LLM

my_llm = load_LLM("us.anthropic.claude-3-5-sonnet-20240620-v1:0")

searcher_agent = Agent(
    role="Content Searcher",
    goal="Search for online content about {topic}",
    backstory="""
                You will research online and find the information about the given topic.
                Get the information back to the user
                """,
    llm=my_llm,
    verbose=True,
    allow_delegate=False,
    tools=[search_tool],
)

summarizer_agent = Agent(
    role="Summarizer",
    goal="Summarize the given text in 20 words",
    backstory="""
                You will create a short summary of the given text with in 20 words.
                The summary should be engaging and informative, maintaining factual accuracy
                """,
    llm=my_llm,
    verbose=True,
    allow_delegate=False,
)

tts_agent = Agent(
    role="text to speech convertor",
    goal="Convert the text to speech and store it in the directory {file_path_tts}",
    backstory="""
                You will convert the text provided to you into an audio format.
                You will store the audio file in the provided directory.
                """,
    llm=my_llm,
    verbose=True,
    allow_delegate=False,
    tools=[tts],
)

manager = Agent(
    role="Process manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="""
    Research into given topic.
    You have to search the internet for that topic and summarize it, then convert that summary into audio and write the audio into the provided directory
    User Input:
    Topic: {topic}
    File Path to save the text to speech file: {file_path_tts}
    """,
    llm=my_llm,
    verbose=True,
    allow_delegation=True,
)
