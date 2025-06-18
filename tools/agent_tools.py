from crewai.tools import tool
from langchain.tools import DuckDuckGoSearchRun
import soundfile as sf

from models.models import load_speech_synthesis_model

synthesiser, speaker_embedding = load_speech_synthesis_model()


def tts_test(text: str, file_path_tts: str) -> str:
    """This function takes in a text and file path and convert the it to speech and write the audio file in the file_path_tts"""
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    sf.write(file_path_tts, speech["audio"], samplerate=speech["sampling_rate"])
    return "Text to speech was completed"


@tool("text to speech")
def tts(text: str, file_path_tts: str) -> str:
    """This function takes in a text and file path and convert the it to speech and write the audio file in the file_path_tts"""
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    sf.write(file_path_tts, speech["audio"], samplerate=speech["sampling_rate"])
    return "Text to speech was completed"


@tool("DuckDuckGoSearch")
def search_tool(search_query: str):
    """Search the web for information on a given topic"""
    search_tool = DuckDuckGoSearchRun()
    return DuckDuckGoSearchRun().run(search_query)
