# Flask Terminal CV 💻☁️

A modern, interactive CV/portfolio website with a terminal-inspired design. Built with Flask and featuring a functional terminal interface for contact.

## ✨ Features

- **Terminal-Style Interface**: Minimalist CLI-inspired design
- **Interactive Contact Terminal**: Real terminal that accepts commands and sends emails
- **Social Links Section**: Direct links to GitHub, LinkedIn, CV PDF, and certifications
- **Scrollable Projects Grid**: Showcase your GitHub projects with tech tags
- **Responsive Design**: Works on all devices
- **Modern Animations**: Smooth typing effects and hover animations

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/xurxox/flask-terminal-cv.git
cd flask-terminal-cv
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5050
```

## 📁 Project Structure

```
flask_terminal_cv/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # This file
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   └── cv_xurxox.pdf          # Your CV (add your own)
└── templates/
    ├── base.html              # Base template
    ├── welcome.html           # Home page with projects
    ├── home.html              # Terminal mode page
    ├── about.html             # About page
    ├── projects.html          # Projects page
    └── contact.html           # Interactive terminal contact
```

## 🎨 Customization

### 1. Update Personal Information

Edit `templates/welcome.html` and `templates/contact.html`:
- Replace "xurxox" with your name/username
- Update GitHub, LinkedIn URLs
- Change email address
- Update location

### 2. Add Your Projects

In `templates/welcome.html`, modify the projects grid:
```html
<div class="project-card">
    <div class="project-header">
        <i class="fas fa-terminal"></i>
        <h3>Your Project Name</h3>
    </div>
    <p class="project-description">
        Your project description
    </p>
    <div class="project-tech">
        <span class="tech-tag">Tech1</span>
        <span class="tech-tag">Tech2</span>
    </div>
    <a href="https://github.com/yourusername/project" target="_blank" class="project-link">
        View on GitHub <i class="fas fa-external-link-alt"></i>
    </a>
</div>
```

### 3. Add Your CV PDF

Place your CV PDF file in the `static/` folder and name it `cv_xurxox.pdf`, or update the link in `welcome.html`.

### 4. Update Colors

Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --page-bg: #0f172a;
    --accent: #38bdf8;
    --accent2: #a855f7;
    /* ... more variables */
}
```

## 🔧 Interactive Terminal Commands

In the contact page, users can type these commands:

- `pwd` - Show current directory
- `ls` or `ls -la` - List files
- `cat info.txt` - Display contact information
- `mail` - Open email form
- `help` - Show available commands
- `clear` - Clear terminal
- `exit` - Exit message

## 📧 Email Integration

The contact terminal includes a simulated email endpoint. To integrate real email sending:

1. Install an email service library (SendGrid, AWS SES, etc.):
```bash
pip install sendgrid
# or
pip install boto3  # for AWS SES
```

2. Update the `/send-email` endpoint in `app.py`:
```python
@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    # Add your email service integration here
    # Example: SendGrid, AWS SES, SMTP, etc.
    pass
```

## 🌐 Deployment

### Deploy to Heroku

1. Install Heroku CLI
2. Create a `Procfile`:
```
web: gunicorn app:app
```
3. Add `gunicorn` to `requirements.txt`:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```
4. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy to AWS EC2

1. SSH into your EC2 instance
2. Clone and setup the project
3. Use Nginx + Gunicorn for production:
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Deploy to Vercel/Railway

Both platforms support Flask. Check their respective documentation for Flask deployment.

## 🎯 Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6
- **Fonts**: Fira Mono (Google Fonts)
- **Design**: Terminal/CLI-inspired minimalist aesthetic

## 📝 License

MIT License - feel free to use this project for your own portfolio!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📮 Contact

- GitHub: [@xurxox](https://github.com/xurxox)
- LinkedIn: [/in/xurxox](https://linkedin.com/in/xurxox)
- Email: xurxox@example.com

---

Made with ☕ and 💻 by Xurxox
