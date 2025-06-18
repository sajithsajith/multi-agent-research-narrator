import torch
from transformers import pipeline
from datasets import load_dataset
from crewai import LLM


def load_speech_synthesis_model():
    """
    Load the speech synthesis model and the speaker embedding.

    Returns:
        synthesiser: The text-to-speech pipeline.
        speaker_embedding: The speaker embedding tensor.
    """

    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation"
    )
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    return synthesiser, speaker_embedding


def load_LLM(model_name="us.anthropic.claude-3-5-sonnet-20240620-v1:0"):
    """
    Load the language model.

    Args:
        model_name (str): The name of the model to load.

    Returns:
        llm: The loaded language model.
    """
    my_llm = LLM(
        model=model_name,
    )
    return my_llm
