# AI Job Intelligence & Resume Matching System

An AI-powered job intelligence system that transforms unstructured resumes into structured career intelligence with explainable job matches.

---

## What This Project Does

Unlike traditional job search platforms that act as simple search engines, this system provides:

- **Deep Resume Analysis**: Extracts and normalizes technical and soft skills from PDF resumes
- **Intelligent Role Inference**: Uses LLM reasoning to determine suitable job roles based on extracted skills
- **Smart Job Matching**: Matches resumes against job descriptions using hybrid deterministic logic and AI reasoning
- **Explainable Recommendations**: Generates human-readable explanations for each job match
- **Skill Gap Analysis**: Shows matched and missing skills for each opportunity
- **Ranked Results**: Provides a ranked list of job opportunities with match scores

---

## Key Features

- **LangGraph Pipeline**: Multi-step reasoning workflow with 6 distinct nodes
- **MCP Server**: Model Context Protocol for tool-based AI orchestration
- **State Management**: Explicit state tracking through the entire pipeline
- **Error Handling**: Each node handles errors independently without breaking the pipeline
- **Pluggable Job Providers**: Mock data included, easily replaceable with real APIs
- **Hybrid Matching**: Combines deterministic skill overlap scoring with LLM-based explanations

---

## Technologies Used

- **Python** - Core programming language
- **LangGraph** - Multi-step reasoning workflow with state management
- **LangChain** - Prompt orchestration (used selectively)
- **OpenAI API** - Resume understanding and reasoning
- **Streamlit** - User interface for resume upload and result visualization
- **PyMuPDF (fitz)** - PDF text extraction
- **MCP** - Model Context Protocol for AI tool orchestration

---

## Project Structure

```
Job_Recommender_System_with_MCP/
├── core/                      # Core intelligence engine
│   ├── graph.py              # LangGraph workflow definition
│   ├── nodes/                # Individual reasoning nodes
│   │   ├── ingest_node.py    # PDF text extraction
│   │   ├── extract_node.py   # Skill extraction (LLM)
│   │   ├── infer_node.py     # Role inference (LLM)
│   │   ├── provider_node.py  # Job data fetching
│   │   ├── match_node.py     # Resume-job matching
│   │   └── explain_node.py   # Explanation generation (LLM)
│   └── providers/            # Data providers
│       └── job_provider.py   # Mock job database
├── src/                      # Legacy helper functions
├── Understanding/            # Detailed documentation
├── app.py                    # Streamlit UI
├── mcp_server.py            # MCP server with tools
├── .env                     # API keys
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Job_Recommender_System_with_MCP
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API key**
   - Open `.env` file in the project root
   - Replace `YOUR_API_KEY_HERE` with your OpenAI API key
   ```bash
   OPENAI_API_KEY="your-actual-api-key-here"
   ```

---

## How to Run

### Option 1: Run Streamlit UI (Recommended)

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Option 2: Run MCP Server

```bash
python mcp_server.py
```

The MCP server will be available for tool-based integration.

---

## Usage

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Upload your resume**
   - Click "Browse files" and select a PDF resume

3. **View analysis**
   - The system will automatically:
     - Extract text from your resume
     - Identify your skills
     - Infer suitable job roles
     - Find matching jobs
     - Generate explanations for each match

4. **Explore results**
   - **Extracted Skills**: See what skills were found in your resume
   - **Inferred Roles**: Discover job roles you're suited for
   - **Job Matches**: View ranked job opportunities with:
     - Match score percentage
     - Matched skills (what you have)
     - Missing skills (what to learn)
     - AI explanations (why you're a good fit)

---

## Demo

<!-- 
   DEMO IMAGE SECTION
   Add screenshots of the application here:
   - Resume upload screen
   - Results display with skills, roles, and job matches
   - Example of match explanation
   
   Example markdown:
   
   ![Demo Screenshot](images/demo.png)
   
   *Screenshot showing the job matching interface*
-->

---

## Pipeline Architecture

The system uses a 6-node LangGraph pipeline:

1. **Ingest Node**: Extract text from PDF resume
2. **Extract Node**: Use LLM to identify skills
3. **Infer Node**: Use LLM to infer suitable job roles
4. **Provider Node**: Fetch job descriptions (currently mock data)
5. **Match Node**: Calculate match scores using deterministic logic
6. **Explain Node**: Generate human-readable explanations using LLM

Each node receives and updates a shared state, ensuring data flows cleanly through the pipeline with error handling at each step.

---

## Configuration

### OpenAI API Key

Required for:
- Skill extraction
- Role inference
- Match explanation generation

Add to `.env`:
```bash
OPENAI_API_KEY="sk-..."
```

Get your API key from: https://platform.openai.com/api-keys

---

## Documentation

For detailed explanations of the project, see the `Understanding/` folder:

- **`project_overview.md`**: What the project does, why it exists, and key architectural decisions
- **`code_file_explanations.md`**: Detailed explanation of every code file and its logic
- **`execution_flow.md`**: Step-by-step execution flow from resume upload to results
- **`file_creation_order.md`**: Build order and why that order matters

---

## Design Principles

- **Not Prompt-Based**: Structured reasoning pipeline instead of single LLM prompts
- **Explainable**: Every recommendation is justified with clear explanations
- **Extensible**: Job providers, models, and nodes are replaceable
- **Failure-Aware**: Each step handles its own errors without breaking the pipeline
- **Production-Minded**: Clean separation of concerns between UI, reasoning, and data

---

## Future Enhancements

- **Real Job APIs**: Replace mock data with LinkedIn, Naukri, Indeed APIs
- **Multiple LLM Support**: Add support for Claude, Gemini, and other models
- **User Profiles**: Save user profiles and track recommendation history
- **Skill Development**: Generate personalized learning paths based on skill gaps
- **Company Research**: Add company information and culture fit analysis
- **Salary Estimates**: Include salary range predictions for matched roles

---

## Troubleshooting

### "OpenAI API key not found"
- Ensure `.env` file exists in the project root
- Verify `OPENAI_API_KEY` is set correctly
- Restart the application after adding the API key

### "ModuleNotFoundError: No module named 'langgraph'"
- Run `pip install -r requirements.txt`
- Ensure your virtual environment is activated

### PDF text extraction issues
- Ensure the PDF is text-based (not scanned images)
- Try extracting text from different pages
- Check that the PDF is not password-protected

---

## License

See `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

## Acknowledgments

This project demonstrates:
- Practical use of LangGraph for multi-step AI reasoning
- Justified use of MCP for AI tool orchestration
- Real-world system design thinking
- Explainable AI applied to career intelligence

**This is not a resume parser. It is a job intelligence system.**

---

## Contact

For questions or support, please open an issue on GitHub.