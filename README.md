# ATS Resume Analyzer API

[![Demo Video](https://img.shields.io/badge/🎥%20Demo-Video-blue?style=flat-square&logo=googledrive)](https://drive.google.com/file/d/1kAJjkmc476nPm8HNkAvzGTN_YPevHOfD/view?usp=sharing)

## Overview

An advanced AI-powered ATS (Applicant Tracking System) resume analyzer built with FastAPI and Google's Gemini AI. This system provides comprehensive resume analysis through two distinct modes: job-specific matching and general ATS optimization. The analyzer uses a sophisticated multi-stage ReAct (Reasoning and Acting) chaining approach to deliver detailed feedback and actionable insights.

## Key Features

### Dual Analysis Modes
- **Job Matching Analysis**: Compares resume against specific job descriptions
- **ATS-Only Analysis**: Focuses on ATS compatibility and optimization without job requirements

### Advanced AI Processing
- **Multi-Stage ReAct Chaining**: Three-step analysis process for comprehensive evaluation
- **Vision + Text Analysis**: Processes both PDF text content and visual layout
- **Gemini 2.0 Flash Integration**: Latest Google AI model for accurate analysis

### Comprehensive Feedback System
- **Category-Based Scoring**: Content, Format, Sections, Skills, and Style evaluation
- **Issue Severity Classification**: Error, Warning, and Info level feedback
- **Actionable Suggestions**: Specific recommendations for improvement
- **ATS Parse Rate**: Percentage-based readability assessment

### Resume Section Generation
- **Dynamic Section Creation**: AI-powered generation of resume sections
- **Question-Answer Processing**: Converts Q&A format into structured resume data
- **Multiple Section Support**: Header, Summary, Experience, Education, Skills, and more

## Technical Architecture

### Core Technologies
- **FastAPI**: High-performance web framework
- **Google Gemini AI**: Advanced language and vision model
- **PyMuPDF**: PDF text extraction and image conversion
- **Pydantic**: Data validation and serialization
- **PIL/Pillow**: Image processing

### Analysis Pipeline

#### Stage 1: Extraction & Structure Analysis
```python
# Initial extraction of resume content
- Basic information extraction
- Education and experience parsing  
- Skills and qualifications identification
- Structure and format analysis
- ATS readability assessment
```

#### Stage 2A: Job Matching Analysis
```python
# Job description comparison
- Key skills mapping
- Experience relevance scoring
- Education requirements matching
- Keyword analysis and gaps
- Overall match percentage calculation
```

#### Stage 2B: ATS Optimization Analysis
```python
# ATS compatibility assessment
- Format issue detection
- Keyword optimization analysis
- Section structure evaluation
- Problematic element identification
- Readability scoring
```

#### Stage 3: Comprehensive Feedback
```python
# Final scoring and recommendations
- Category-wise scoring (0-100)
- Issue identification with severity
- Detailed analysis per category
- Actionable improvement suggestions
- Overall assessment and ratings
```

## API Endpoints

### 1. Job Matching Analysis
```http
POST /analyze/job-matching/
Content-Type: multipart/form-data

Parameters:
- resume_file (PDF file)
- job_description (string)
```

**Response Structure:**
```json
{
  "overall_score": 85,
  "ats_parse_rate": 92,
  "match_percentage": 78,
  "categories": [
    {
      "category": "content",
      "score": 88,
      "issues_found": 2,
      "issues": [...],
      "analysis": "Detailed analysis...",
      "suggestions": [...]
    }
  ]
}
```

### 2. ATS-Only Analysis
```http
POST /analyze/ats-only/
Content-Type: multipart/form-data

Parameters:
- resume_file (PDF file)
```

**Response Structure:**
```json
{
  "overall_score": 83,
  "ats_parse_rate": 95,
  "potential_improvement": 12,
  "categories": [...]
}
```

### 3. Resume Section Generation
```http
POST /generate_resume_section
Content-Type: application/json

Body:
{
  "sectionName": "experience",
  "questionAnswers": {
    "What was your job title?": "Software Engineer",
    "Company name?": "Tech Corp"
  }
}
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Google API Key for Gemini
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd ats-resume-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn python-multipart
pip install google-generativeai PyMuPDF Pillow
pip install python-dotenv pydantic
```

4. **Set up environment variables**
```bash
# Create .env file
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

5. **Run the application**
```bash
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Configuration

### Environment Variables
```env
GOOGLE_API_KEY=your_gemini_api_key
```

### Model Configuration
```python
generation_config = {
    "temperature": 0.2,      # Creativity vs consistency
    "top_p": 0.95,          # Nucleus sampling
    "top_k": 40,            # Top-k sampling
    "max_output_tokens": 8192  # Response length limit
}
```

## Supported Resume Sections

The system supports generation and analysis of multiple resume sections:

- **Header**: Name, contact, professional role
- **Summary**: Professional summary and objectives  
- **Education**: Degrees, institutions, dates, GPA
- **Experience**: Job titles, companies, responsibilities
- **Projects**: Project details, technologies, roles
- **Skills**: Technical and soft skills categorization
- **Certificates**: Certifications with links and dates
- **Achievements**: Awards and accomplishments
- **Interests**: Personal interests and hobbies
- **Languages**: Language proficiency levels

## Analysis Categories

### Content Analysis
- Relevance to job requirements
- Keyword optimization
- Information completeness
- Achievement quantification

### Format Analysis
- ATS compatibility
- Visual layout assessment
- Font and spacing consistency
- Header/footer usage

### Section Analysis
- Proper section organization
- Essential sections presence
- Information hierarchy
- Section completeness

### Skills Analysis
- Skill relevance and currency
- Technical vs soft skills balance
- Skill presentation format
- Industry-specific keywords

### Style Analysis
- Professional tone
- Grammar and spelling
- Consistency in tense and format
- Overall presentation quality


---

**Transform your resume analysis with AI-powered insights and ATS optimization!**
