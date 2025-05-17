# Universal LLM API Service

A flexible FastAPI-based backend for interacting with multiple Large Language Model (LLM) providers—including OpenAI, Anthropic, and Llama—using a unified REST API. Easily integrate, extend, and secure multimodal LLM capabilities in your applications.

---

## Features

- **Unified API Endpoint** for chat completion across providers (OpenAI, Anthropic, Llama)
- **Provider-Aware Parameter Handling:** Automatic adaptation of parameters (like `temperature`, `top_p`) per model requirements
- **CORS Enabled:** Safe cross-origin access for web frontends
- **Simple Routing:** Health/ping endpoint and `/llm_model/` chat endpoint
- **Secure by Design:** Integration with external authentication (token validation via IAM)
- **Structured Logging:** Centralized and contextual logging for API and provider calls
- **Async-Ready:** Fully async for performance with modern Python web servers

---

## Project Structure

```txt
.
├── main.py          # FastAPI app, CORS, router setup
├── routes/
│   ├── llm.py       # /llm_model/ endpoint, dispatch to providers
│   └── ping.py      # Healthcheck endpoint
├── utils.py         # LLM service classes, authentication, utilities
├── logger.py        # Logging setup and utility
├── settings.py      # Environment variables, API keys, paths
├── requirements.txt # Python dependencies
└── README.md        # Project documentation (this file)
```

---

## Quick Start

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

> Requirements include: `fastapi`, `uvicorn`, `openai`, `anthropic`, (Llama Python bindings), `requests`, etc.

### 2. Configure Environment

Set the following in your `settings.py` or as environment variables:

- `OPEN_AI_API_KEY`
- `ANTHROPIC_API_KEY`
- `LLAMA_CKPT_DIR`
- `LLAMA_TOKENIZER_PATH`
- IAM integration:
  - `IAM_API_SERVER_URL`
  - `IAM_CUSTOMER_SECRET_KEY`
  - `IAM_APP_IDENTIFIER`

### 3. Run the Server

```bash
python main.py
```

The server runs at `http://0.0.0.0:8000`

---

## API Usage

### 1. Health Check

```http
GET /ping/
```

---

### 2. LLM Model Chat

```http
POST /llm_model/
Content-Type: application/json
Authorization: Bearer <token>         # (Required if IAM is enabled)

{
  "model_name": "gpt-3.5-turbo",      # LLM model name
  "message": [                        # Message format varies per provider
    {"role": "user", "content": "Hello!"}
  ],
  "service_provider": "openai",       # "openai" | "anthropic" | "llama"
  "output_format": "text",            # (optional) Output format
  "temprature": 0.9,                  # (optional) Sampling temperature
  "max_output_token": 2048,           # (optional) Max output tokens
  "top_p": 0.9                        # (optional) Nucleus sampling
}
```

- **Provider options**:  
  - `"openai"`: Supports temperature, top_p, output_format.
  - `"anthropic"`: Supports temperature, top_p, messages as per Anthropic's format.
  - `"llama"`: Local inference, supports temperature, top_p.

#### Example (OpenAI)

```http
POST /llm_model/
{
  "model_name": "gpt-4",
  "message": [{"role": "user", "content": "Summarize this text..."}],
  "service_provider": "openai"
}
```

#### Example (Anthropic)

```http
POST /llm_model/
{
  "model_name": "claude-3-opus-20240229",
  "message": [{"role": "user", "content": "Explain quantum computing simply."}],
  "service_provider": "anthropic"
}
```

#### Example (Llama)

```http
POST /llm_model/
{
  "model_name": "llama_model", #You can download any model locaaly and test it
  "message": "What's the weather like in Paris?",
  "service_provider": "llama"
}
```

---

### 3. Response Structure

- On **success**:
  ```json
  {
    "success": true,
    "output": { ... }   // Provider-specific output
  }
  ```
- On **error**:
  ```json
  {
    "success": false,
    "message": "Internal Server Error",
    "error": "<traceback or error message>"
  }
  ```

---

## Extending & Customizing

- **Add new providers**: Create a new service class in `utils.py`, add handler logic to `llm.py`.
- **Authentication**: Toggle user authentication by enabling/disabling IAM code in `llm.py`.
- **Logging**: Customize logger output in `logger.py`.

---

## Notes

- **Token Validation** is implemented but commented out in the endpoint for easy switch between environments.
- **Llama Integration** assumes local models and inference; ensure correct model/checkpoint paths and hardware support.
- **Async**: All provider calls are designed to be async for performance.

---

## License

MIT License

---

## Authors

- Arjunsingh Kuldeepsingn Rana
- Inspired by modern API integration patterns for LLMs

---

## Contributing

Pull requests and issues are welcome! Please open a discussion or PR for new model providers or features.
