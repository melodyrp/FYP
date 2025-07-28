# FYP  
Team 0064 FYP  
**ETHICAL HACKING OF LARGE LANGUAGE MODELS: EXPLORING VULNERABILITIES AND MITIGATION TECHNIQUES**

---

## FYP Project ChatBots: Attack & Defence Versions

This project contains two versions of a multi-LLM chatbot built using **Streamlit**, focusing on prompt injection research and defense testing. Each chatbot supports:

- **Google Gemini 1.5**
- **OpenAI GPT-4**
- **Local Ollama LLaMA 3.2**

The bots are designed for **educational** and **adversarial testing** purposes, simulating both **prompt injection attack behaviors** and **defensive mitigation strategies**.

---

## ChatBot Variants

### `attack_combined.py`
Simulates **vulnerable chatbot behavior** for red team testing.
- Minimal or no guardrails
- Dropdown menu for selecting **attack type**:
  - Prompt Injection
  - Prompt Leaking
  - Jailbreak
- Sidebar library of curated attack prompts for testing
- Designed to intentionally be bypassed

### `defence_combined.py`
Implements **defensive countermeasures** to secure chatbot interaction.
#### Key Features:
- ✅ **Prompt Injection & Jailbreak Detection**
- ✅ **Output Filtering** for LLM07 (System Prompt Leakage) and LLM02 (Sensitive Info Disclosure)
- ✅ **Regex-based Input Filtering** to block malicious CSV-style or obfuscated payloads (LLM08)
- ✅ **Context Isolation** and denial of role-switching prompts
- ✅ **Admin-only Access Controls** for file-based data (enabled only on LLaMA 3.2)
- ✅ **Terminal Logging System** for:
  - Blocked prompts
  - Suspicious input/output events
  - Exporting logs to `.txt` for audit trail
- ✅ **UI Feedback** with warning messages when malicious patterns are detected
- 🖌️ Blue-themed professional UI with chat bubbles and model role styling

---

## Project Structure
├── data/ # Internal CSVs and component files for LLaMA 3.2
├── terminal_log/ # (Auto-created) directory for exported terminal logs
├── .env # Gemini API key
├── apaikey.env # OpenAI API key
├── attack_combined.py # Insecure version simulating vulnerabilities
├── attack_combined_originalbackup.py # Backup of initial attack bot
├── defence_combined.py # Secure version with logging and defenses
├── README.md # You are here


---

## Research Highlights
- Supports testing of OWASP LLM Top 10:  
  - LLM01: Prompt Injection  
  - LLM02: Sensitive Information Disclosure  
  - LLM07: System Prompt Leakage  
  - LLM08: Vector Weaknesses  
  - LLM09: Context Poisoning  
  - LLM10: Unbounded Consumption

- Demonstrated both **successful exploits** and **working defenses** using Mistral (archived), GPT-4, Gemini, and LLaMA 3.2.

---

> Built by Team 0064  
> Final Year Project – Republic Polytechnic  
> For educational, ethical, and cybersecurity research purposes only.
