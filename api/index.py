from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import PyPDF2
from docx import Document
import io
import re
import random

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*"  # For development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_text_from_pdf(file_bytes):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"PDF extraction error: {str(e)}")
        return ""


def extract_text_from_docx(file_bytes):
    """Extract text from Word file"""
    try:
        doc = Document(io.BytesIO(file_bytes))
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"DOCX extraction error: {str(e)}")
        return ""


def detect_sections(cv_text):
    """Detect CV sections without AI"""
    sections = []
    
    # Define section keywords and their variations
    section_patterns = {
        "Personal Information": ["personal", "contact", "profile", "about me", "summary"],
        "Education": ["education", "academic", "qualification", "degree", "university", "college", "school"],
        "Experience": ["experience", "employment", "work history", "professional", "career", "job"],
        "Skills": ["skills", "technical skills", "competencies", "technologies", "expertise", "proficient"],
        "Projects": ["projects", "portfolio", "work samples", "achievements"],
        "Certifications": ["certification", "certificate", "training", "course"],
        "Languages": ["languages", "linguistic"],
        "Interests": ["interests", "hobbies", "activities"]
    }
    
    cv_lower = cv_text.lower()
    
    for section_name, keywords in section_patterns.items():
        for keyword in keywords:
            # Find keyword position
            pattern = rf'\b{keyword}s?\b'
            match = re.search(pattern, cv_lower)
            
            if match:
                start_idx = match.start()
                # Extract content (next 300 characters)
                end_idx = min(start_idx + 300, len(cv_text))
                content = cv_text[start_idx:end_idx].strip()
                
                sections.append({
                    "title": section_name,
                    "content": content
                })
                break  # Found this section, move to next
    
    # If no sections found, create a generic one
    if not sections:
        sections.append({
            "title": "General",
            "content": cv_text[:500]
        })
    
    return sections


def generate_malayalam_troll(section_title, section_content):
    """Generate funny Malayalam troll WITHOUT any AI API"""
    
    # Pre-written Malayalam trolls for each section
    trolls = {
        "Personal Information": [
            "പേര്, വിലാസം, ഫോൺ നമ്പർ... അത്രേ ഉള്ളൂ! ഇതൊക്കെ WhatsApp status-ൽ പോസ്റ്റ് ചെയ്യാൻ പറ്റുമോ? 😂",
            "Personal Info കണ്ടാൽ തോന്നും LinkedIn profile കോപ്പി അടിച്ചതാണെന്ന്! കുറച്ചു creativity വേണമായിരുന്നു! 🤔",
            "Contact details മാത്രം കൊടുത്തിട്ട് എന്താ കാര്യം? ഇതിനേക്കാൾ നല്ല ഒരു intro വേണ്ടേ? 😅"
        ],
        
        "Education": [
            "എഡ്യൂക്കേഷൻ സെക്ഷൻ കണ്ടാൽ തോന്നും വിക്കിപീഡിയയിൽ നിന്ന് കോപ്പി അടിച്ചതാണെന്ന്! കോളേജ് പേര് വലുതാണ്, പക്ഷേ marks എവിടെ? 😂",
            "Degree-യുടെ പേര് കേട്ടാൽ impressive ആണ്, പക്ഷേ പഠിച്ചത് എന്താണെന്ന് Google-ൽ search ചെയ്യണം! 🎓😄",
            "University പേര് കണ്ടിട്ട് ആരും impressed ആകില്ല! എന്താണ് പഠിച്ചതെന്ന് പറഞ്ഞാൽ മതി! 📚🤨"
        ],
        
        "Experience": [
            "Experience എന്ന് പറയുമ്പോൾ company വെബ്സൈറ്റിൽ നിന്ന് job description കോപ്പി-പേസ്റ്റ് ചെയ്തതാണെന്ന് മനസ്സിലാവുന്നുണ്ട്! എന്താണ് ചെയ്തതെന്ന് വ്യക്തമായി പറയാൻ ഭയമാണോ? 🤔",
            "2 വർഷം experience എന്ന് പറഞ്ഞാൽ office-ൽ ചായ കുടിച്ച experience ആണോ? നേട്ടങ്ങൾ എവിടെ? ☕😂",
            "Job responsibilities കണ്ടാൽ ChatGPT എഴുതി കൊടുത്തതാണെന്ന് തോന്നുന്നു! Real work എന്താണ്? 💼🤖"
        ],
        
        "Skills": [
            "Skills ലിസ്റ്റിൽ എല്ലാം ഉണ്ട് - Python, Java, AI, ML, Blockchain! അടുത്തതായി 'Time Travel' കൂടി ചേർത്താൽ മതിയായിരുന്നു! 🚀😄",
            "100+ skills ഉണ്ടെന്ന് claim ചെയ്യുന്നു, പക്ഷേ 'Hello World' എഴുതാൻ അറിയുമോ എന്ന് സംശയം! 👨‍💻😅",
            "Skill level ഒന്നും mention ചെയ്തിട്ടില്ല! Beginner level skills-നെ expert level എന്ന് വിളിക്കുകയാണോ? 📊🙄"
        ],
        
        "Projects": [
            "Projects കണ്ടാൽ തോന്നും YouTube tutorial കണ്ടു കോപ്പി അടിച്ചതാണെന്ന്! GitHub link ഇല്ലാത്തത് എന്തിന്? Code നോക്കിയാൽ പേടിയാണോ? 😅",
            "Project description വായിച്ചാൽ Stack Overflow answers paste ചെയ്തതാണെന്ന് മനസ്സിലാവും! Original work എവിടെ? 💻🤔",
            "Projects section-ൽ college assignments ആണെന്ന് പറയാതെ 'Major Projects' എന്ന് എഴുതിയിരിക്കുന്നു! 🎯😂"
        ],
        
        "Certifications": [
            "Certificate കിട്ടാൻ Udemy-യിൽ ₹399 കൊടുത്തു എന്ന് മനസ്സിലാവുന്നുണ്ട്! അതിനേക്കാൾ വലിയ നേട്ടം ജീവിതത്തിൽ ഇല്ലേ? 🏆😂",
            "Online certification കണ്ടാൽ തോന്നും weekend-ൽ bore അടിച്ചപ്പോൾ ചെയ്തതാണെന്ന്! Real skill ഉണ്ടോ? 📜🤨",
            "Certificate-ന്റെ പേര് വലുതാണ്, പക്ഷേ actually പഠിച്ചത് എന്താണെന്ന് ആരും ചോദിക്കരുത്! 🎓😄"
        ],
        
        "Languages": [
            "Languages known എന്ന് എഴുതിയിട്ട് 'English: Intermediate' എന്ന് പറയുന്നു! WhatsApp-ൽ 'k' എന്ന് മാത്രം type ചെയ്യുന്നവർക്ക് intermediate ആണോ? 🗣️😂",
            "മലയാളം, English, Hindi അറിയാം എന്ന് പറയുന്നു! Google Translate use ചെയ്യുന്നത് language skill അല്ലല്ലോ! 🌐😅"
        ],
        
        "Interests": [
            "Hobbies: Reading, Traveling, Music എന്ന് generic ആയി എഴുതിയിരിക്കുന്നു! Instagram scroll ചെയ്യുന്നത് hobby ആണെന്ന് പറയാൻ മടിയാണോ? 📱😂",
            "Interests കണ്ടാൽ ഒരു CV template-ൽ നിന്ന് കോപ്പി അടിച്ചതാണെന്ന് തോന്നുന്നു! Original interest ഇല്ലേ? 🎨🤔"
        ],
        
        "General": [
            "CV മൊത്തത്തിൽ നോക്കിയാൽ ChatGPT-യോട് 'എനിക്ക് ഒരു CV തരൂ' എന്ന് ചോദിച്ചതാണെന്ന് തോന്നുന്നു! 😂",
            "എല്ലാ section-ലും generic content മാത്രം! Personality എവിടെ? 🤷‍♂️",
            "CV formatting കണ്ടാൽ 2005-ൽ ആണോ create ചെയ്തതെന്ന് തോന്നുന്നു! Modern design വേണമായിരുന്നു! 🎨😅"
        ]
    }
    
    # Get trolls for the section
    section_trolls = trolls.get(section_title, trolls["General"])
    
    # Return random troll from the list
    return random.choice(section_trolls)


@app.post("/api/troll_cv")  # Changed from /api/troll_cv
async def troll_cv(file: UploadFile = File(...)):
    """Main endpoint to process CV and return trolling text"""
    print(f"\n📁 Received file: {file.filename}")
    
    try:
        file_bytes = await file.read()
        print(f"📊 File size: {len(file_bytes)} bytes")
        
        # Extract text based on file type
        if file.filename.endswith('.pdf'):
            cv_text = extract_text_from_pdf(file_bytes)
        elif file.filename.endswith(('.docx', '.doc')):
            cv_text = extract_text_from_docx(file_bytes)
        else:
            return JSONResponse(
                status_code=400,
                content={"error": "Unsupported file format. Please use PDF or DOCX"}
            )
        
        if not cv_text or len(cv_text) < 50:
            return JSONResponse(
                status_code=400,
                content={"error": "Could not extract text from file."}
            )
        
        sections = detect_sections(cv_text)
        
        trolled_sections = []
        for section in sections[:6]:
            troll_text = generate_malayalam_troll(
                section["title"], 
                section["content"]
            )
            trolled_sections.append({
                "title": section["title"],
                "troll": troll_text
            })
        
        return JSONResponse(content={
            "success": True,
            "trolled_sections": trolled_sections
        })
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Server error: {str(e)}"}
        )

@app.get("/")
def read_root():
    return {"message": "CV Troll Malayalam API is running! 🚀"}



@app.get("/api/test")
def test_endpoint():
    return {
        "status": "success",
        "message": "API is working perfectly! ✅",
        "malayalam_test": "മലയാളം ടെസ്റ്റ് വർക്ക് ചെയ്യുന്നു!"
    }
