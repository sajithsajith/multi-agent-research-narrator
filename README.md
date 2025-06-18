# 🤖 Agentic TTS Crew: Autonomous Research to Speech Synthesis

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Framework: CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange.svg?logo=rocket&logoColor=white)](https://www.crewai.com/)
[![Framework: Hugging Face](https://img.shields.io/badge/Framework-Hugging%20Face-FCC624.svg?logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Framework: LangChain](https://img.shields.io/badge/Framework-LangChain-00A37F.svg?logo=langchain&logoColor=white)](https://www.langchain.com/)
[![LLM](https://img.shields.io/badge/LLM-Claude%203.5%20Sonnet-purple.svg)](https://www.anthropic.com/news/claude-3-5-sonnet)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project showcases a powerful multi-agent system built with **CrewAI** that automates the process of researching any given topic, generating a concise summary, and converting that summary into a high-quality spoken audio file.

The crew works autonomously, with a manager agent orchestrating a team of specialized agents to achieve the final goal, demonstrating a practical application of agentic workflows.

---

## 🚀 Key Features

- **🧠 Hierarchical Agent Management**: A Manager Agent delegates tasks to specialized agents, ensuring a structured and efficient workflow.
- **🌐 Dynamic Web Research**: The Searcher Agent uses DuckDuckGo to find up-to-date information on any topic.
- **✍️ AI-Powered Summarization**: The Summarizer Agent distills complex information into a brief, engaging summary.
- **🗣️ High-Quality Text-to-Speech**: The TTS Agent leverages Hugging Face's `microsoft/speecht5_tts` model to create natural-sounding speech.
- **☁️ Cloud LLM Integration**: Powered by the state-of-the-art **Anthropic Claude 3.5 Sonnet** via AWS Bedrock.

---

## 📊 How It Works: The Agentic Workflow

The entire process is managed by a hierarchical crew. The Manager Agent receives the initial request and breaks it down, delegating each step to the appropriate specialist agent.

### The Agents

1.  **Content Searcher**: Responsible for scouring the internet to gather relevant information on the user-defined topic.
2.  **Summarizer**: Takes the raw information and crafts a concise, 20-word summary that is both engaging and factually accurate.
3.  **TTS Converter**: Receives the final summary and transforms it into an audio file, saving it to the specified path.
4.  **Process Manager**: The orchestrator. It understands the end-to-end goal and ensures each agent completes its task in the correct sequence.

---

## 🛠️ Technology Stack

- **Core Framework**: [CrewAI](https://www.crewai.com/)
- **LLM**: [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) (via AWS Bedrock)
- **Text-to-Speech**: [Hugging Face Transformers](https://huggingface.co/transformers) (`microsoft/speecht5_tts`)
- **Web Search**: [DuckDuckGo Search](https://duckduckgo.com/)
- **Audio Processing**: [SoundFile](https://pysoundfile.readthedocs.io/)
- **Cloud Platform**: [AWS Bedrock](https://aws.amazon.com/bedrock/)

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

The required packages are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

This project requires AWS credentials to access the Claude 3.5 Sonnet model via Bedrock.

Create a file named `.env` in the root of your project directory and add your credentials:

```env
# .env
AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY"
AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_KEY"
AWS_DEFAULT_REGION="us-east-1" # Or your preferred AWS region
```

**Note**: Ensure the IAM user associated with these credentials has permission to invoke models in AWS Bedrock.

---

## ▶️ How to Run

With the setup complete, you can run the agent crew with a single command. The main script is designed to be easily configurable.

1.  Open the main Python file `test.ipynb`.
2.  Modify the `template_input` dictionary to set your desired `topic` and output `file_path_tts`.

    ```python
        inputs = {
            "topic": "the impact of quantum computing on cryptography",
            "file_path_tts": "quantum_impact.wav"
        }

        result = crew.kickoff(inputs=inputs)

        print("\n✅ Crew execution finished.")
        print("🔊 Final Output:")
        print(result)
    ```

### Example Output

You will see verbose output in your terminal as the agents work, delegate tasks, and use their tools.

```
🚀 Starting the Agentic TTS Crew...

> Entering new CrewAgentExecutor chain...
[Manager Agent]
I need to manage a crew to research a topic, summarize it, and convert it to speech.
The topic is: the impact of quantum computing on cryptography
The output file path is: quantum_impact.wav

First, I will delegate the research task to the Content Searcher.
...
[Content Searcher]
Action: DuckDuckGoSearch
Action Input: ...
...
[Summarizer Agent]
Action: Summarize
Action Input: ...
...
[TTS Agent]
Action: text to speech
Action Input: ...

> Finished chain.

✅ Crew execution finished.
🔊 Final Output:
Text to speech was completed
```

After the run, you will find your audio file (e.g., `quantum_impact.wav`) in the specified directory.

---

## 🎨 Customization

This project is a great starting point. Here are a few ways you can customize and extend it:

- **Change the LLM**: Swap `Claude 3.5 Sonnet` with another model supported by CrewAI, such as one from OpenAI, Groq, or a local Ollama instance.
- **Modify Agent Roles**: Adjust the `role`, `goal`, and `backstory` of any agent to change its behavior and personality.
- **Add New Tools**: Create new custom tools (e.g., for saving the summary to a file, posting to social media) and assign them to the agents.
- **Expand the Crew**: Add more agents to handle more complex tasks, like a `FactCheckerAgent` or a `ReportWriterAgent`.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
