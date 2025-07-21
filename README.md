# FYP
Team 0064 FYP 
ETHICAL HACKING OF LARGE LANGUAGE MODELS: EXPLORING VULNERABILITIES AND MITIGATION TECHNIQUES 

# FYP project ChatBots: Attack & Defence Versions

This project contains two versions of a multi-LLM chatbot built using **Streamlit**, focusing on prompt injection research and defense testing. Each chatbot supports:

- Google Gemini 1.5
- OpenAI GPT-4
- Local Ollama LLaMA 3.2

The bots are intended for **educational** and **adversarial testing** purposes, simulating both **prompt injection attack behaviors** and **defensive prompt strategies**.

---

## ChatBot Variants

### `attack_combined.py`
Simulates **vulnerable chatbot behavior**. It:
- Responds with minimal guardrails
- Includes a dropdown to select different **attack types**:
  - Prompt Injection
  - Prompt Leaking
  - Jailbreak
- Provides example attack prompts in a sidebar prompt library
- Allows users to copy/paste prompts for testing

### `defence_combined.py`
Implements **secure chatbot defense mechanisms**, including but not limited to:
- Response filtering for **LLM08: Sensitive Information Disclosure**
- Input validation to block **LLM05: Unsanitized Inputs**
- Strong system prompts to enforce identity denial, context isolation, and behavior constraints
- Defense awareness embedded in Gemini and LLaMA system prompts
- Blue-themed UI with role-specific styling for professional polish

---

## Project Structure
├── data/ # Internal files used by LLaMA 3.2 (auto-loaded)
├── .env # Gemini API key file
├── apaikey.env # OpenAI API key file
├── attack_combined.py # Insecure version for attack simulation
├── attack_combined_originalbackup.py # Backup copy of the attack version
├── defence_combined.py # Secure version with defensive rules
└── README.md # This file

Built by Team0064


