# 🤣 CV Troll Malayalam

> A hilarious web app that roasts your CV with witty Malayalam commentary!

Upload your resume and get instant, humorous trolling feedback in Malayalam for each section. Built for laughs, learning, and showing off your tech skills!

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/cv-troll-malayalam)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 📄 **PDF & DOCX Support** - Upload resumes in multiple formats
- 🎯 **Section Detection** - Automatically identifies CV sections (Education, Experience, Skills, etc.)
- 😂 **Malayalam Trolling** - Hilarious, pre-written Malayalam roasts for each section
- ⚡ **Lightning Fast** - No AI API calls, instant results
- 🎨 **Beautiful UI** - Modern gradient design with Tailwind CSS
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 🚀 **Zero Cost** - Deploy for free on Vercel

## 🛠️ Tech Stack

### Frontend
- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Turbopack** - Ultra-fast bundler

### Backend
- **FastAPI** - Modern Python web framework
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX parsing
- **Uvicorn** - ASGI server

## 📦 Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- pip

### Clone Repository
`git clone https://github.com/YOUR_USERNAME/cv-troll-malayalam.git`
`cd cv-troll-malayalam`

### Backend Setup

Create virtual environment
`cd api`
`python -m venv venv`

Activate virtual environment
Windows:
`venv\Scripts\activate`

Mac/Linux:
`source venv/bin/activate`

Install dependencies
`pip install -r requirements.txt`

### Frontend Setup
Navigate to project root
`cd ..`

Install dependencies
`npm install`

## 🚀 Running Locally

### Terminal 1: Start Backend
`cd api`
`uvicorn index:app --reload --port 8000`

Backend will run at `http://localhost:8000`

### Terminal 2: Start Frontend
`npm run dev`

Frontend will run at `http://localhost:3000`

## 🎯 How It Works

1. **User uploads CV** (PDF/DOCX) via the web interface
2. **Frontend sends file** to `/api/troll_cv` endpoint
3. **Backend extracts text** using PyPDF2 or python-docx
4. **Section detection** identifies CV sections using keyword matching
5. **Troll generation** selects random Malayalam jokes from pre-written templates
6. **Frontend displays** results in beautiful cards with Malayalam text

## 🌐 Deploy to Vercel

### One-Click Deploy
Click the button at the top of this README to deploy instantly!

### Manual Deploy
nstall Vercel CLI
`npm i -g vercel`

Login
`vercel login`

Deploy
`vercel --prod`

Your app will be live at `https://cv-troll-malayalam.vercel.app`

## 📝 API Endpoints

### `POST /api/troll_cv`
Upload CV and get trolling results

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (PDF or DOCX)

**Response:**
{
"success": true,
"trolled_sections": [
{
"title": "Education",
"troll": "എഡ്യൂക്കേഷൻ സെക്ഷൻ കണ്ടാൽ വിക്കിപീഡിയയിൽ നിന്ന് കോപ്പി അടിച്ചതാണെന്ന് തോന്നുന്നു! 😂"
}
]
}

### `GET /`
Health check endpoint

## 🎨 Screenshots

<!-- Add your screenshots here -->
![CV Upload Interface](./screenshots/upload.png)
![Trolling Results](./screenshots/results.png)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ideas for contributions:**
- Add more Malayalam trolls
- Support for additional CV sections
- Add English language support
- Improve UI/UX
- Add export to PDF feature
- Create browser extension

## 🐛 Known Issues

- Large PDF files (>10MB) may take longer to process
- Some PDF formats with complex layouts may not extract perfectly
- Malayalam fonts may not render correctly on some older browsers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@abhijithkj369](https://github.com/abhijithkj369)
- LinkedIn: [abhijithkj3690](https://www.linkedin.com/in/abhijithkj3690/)

## 🙏 Acknowledgments

- Inspired by the need to make CV reviewing fun
- Malayalam comedy culture and humor
- Open source community

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/cv-troll-malayalam?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/cv-troll-malayalam?style=social)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/cv-troll-malayalam)

## 🔮 Future Enhancements

- [ ] Add AI-powered trolling (GPT-4 integration)
- [ ] Support for more languages (Hindi, Tamil, Telugu)
- [ ] Professional feedback mode
- [ ] Share results on social media
- [ ] Download trolled CV as PDF
- [ ] Chrome extension for LinkedIn profiles
- [ ] User authentication and history
- [ ] Rating system for trolls

## 💡 Related Projects

Check out these similar projects:
- [LinkedIn Profile Analyzer](#)
- [Code Review Roaster](#)
- [GitHub Stats Visualizer](#)

---

**Made with ❤️ and lots of 😂 in Kerala**

⭐ Star this repo if you found it funny!

🐛 Found a bug? [Open an issue](https://github.com/YOUR_USERNAME/cv-troll-malayalam/issues)

🤔 Have questions? [Start a discussion](https://github.com/YOUR_USERNAME/cv-troll-malayalam/discussions)
Additional Files to Create
LICENSE file:
text
MIT License

Copyright (c) 2025 YOUR_NAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.