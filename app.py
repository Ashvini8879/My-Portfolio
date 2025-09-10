from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "ashu4567"
MAIL_USERNAME = ""
MAIL_PASSWORD = ""

# === Dummy project data ===
projects = [
   {
  "id": 1,
  "title": "Tourism Management Web application",
  "image": "tourism.png",
  "language": "Flask, Python, HTML, CSS, JavaScript, SQLite and Razorpay",
  "github": "https://github.com/Ashvini8879/Tourism-Management.git",
  "description": "The Tourism Management System is a comprehensive web application designed to streamline the process of exploring, booking, and managing tours for users while simplifying administrative tasks for tour operators. This platform aims to provide an efficient, user-friendly, and secure solution tailored to the travel industry.",
  "features": "• Explore a wide range of tours with detailed information.<br>• Flexible login systems for users and administrators.<br>• Users: Comment, add to Wishlist, and book tours.<br>• Admins: Add, edit, and delete tour details.<br>• Secure Razorpay payment integration.<br>• Email confirmation on booking.<br>• Scalable and user-friendly design.",
  }
,
    {

 "id": 2,
        "title": "Netflix Data Analysis Dashboard",
        "image": "Netfllix_dash.png",
        "language": "Advanced Excel",
        "github": "https://github.com/Ashvini8879/Netflix-Data-Analysis-Dashboard.git",
        "description": "A web-based Netflix data analysis dashboard developed using Excel and CSV datasets, designed to provide actionable insights on movies and TV shows. The platform allows interactive exploration of content trends, ratings, genres, actors, and countries, helping users understand viewing patterns and content distribution.",
        "features": "• Analyze total movies and TV shows count.<br>• Visualize content type distribution and yearly trends.<br>• Explore top genres, actors, and producing countries.<br>• View rating distribution across content types.<br>• Interactive dashboard with slicers and filters for deep insights.<br>• Cleaned dataset and original CSV/Excel files included for analysis.<br>• Supports future predictive analysis and web-based dashboard integration.",

       
    },
    {
         "id": 3,
        "title": " Blinkit Data Analysis Project",
        "image": "Blinkit.png",
        "language": "Advanced Excel, Python, SQL",
        "github": "https://github.com/Ashvini8879/Blinkit-Data-Analysis.git",
       "description": "A data analysis project using SQL, Python, and Excel to uncover sales insights for Blinkit. The project cleans and processes raw sales data, performs EDA, derives key KPIs, and builds an interactive Excel dashboard for business decision-making.",
       "features": "• Data Cleaning: Standardized categories, handled missing values, and removed duplicates.<br>• SQL Analysis: Derived sales trends, outlet performance, and product-level insights.<br>• Python Visualization: Created charts (bar, line, donut) using pandas, matplotlib, and seaborn.<br>• Interactive Dashboard: Built in Excel with slicers and filters for dynamic analysis.<br>• KPIs: Total Sales, Average Sales, Number of Items, and Ratings by outlet type and location.<br>• Business Insights: Identified top-performing outlets, major sales contributors, and growth trends."
},
 {
    
        "id": 4,
        "title": "Clean City Reporting App",
        "image": "clean.png",
        "language": "Figma Tool",
        "github": "https://github.com/Ashvini8879/Clean-City-Reporting-App-Design.git",
        "description": "A mobile application prototype designed in Figma to promote cleanliness, civic responsibility, and community engagement in Mumbai. The app enables users to report unclean areas with images and descriptions, access educational content, and track complaint resolution status. It fosters a cleaner city through awareness, transparency, and user participation.",
        "features": "• Easy Complaint Submission: Report public littering by uploading photos with descriptions.<br>• Location-Based Tracking: Tag complaints with user location for faster response by authorities.<br>• Educational Content: Learn and share videos promoting cleanliness and hygiene.<br>• Community Interaction: Like, save, and share posts to boost participation.<br>• Help Center: Access support for guidance and queries.<br>• Real-time Status: Track updates on reported issues transparently.",
    },
    {
         "id": 5,
        "title": "Online Job Portal Application",
        "image": "job.png",
        "language": "ASP .NET, C#, HTML, CSS , JavaScript",
        "github": "https://github.com/Ashvini8879/Online-Job-Portal-Application.git",
        "description": "A web-based job portal developed using ASP.NET and SQL Server, designed to streamline the job search and recruitment process. The platform offers dedicated interfaces for job seekers, employers, and administrators, featuring smart job filtering, resume upload, and an automated resume keyword matching system.",
        "features": "• Job Seekers: Register, log in, and manage profiles.<br>• Browse and filter jobs by location, type, and date.<br>• Upload resumes and apply to jobs directly.<br>• Redirect to LinkedIn for more opportunities.<br>• Employers/Admin: Post and manage job listings.<br>• Track applications and access dashboard stats.<br>• Resume Matching System with keyword-based match percentage.",

    }
]

# === Routes ===

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return redirect(url_for("home") + "#about")

@app.route("/projects")
def project_list():
    return render_template("projects.html", projects=projects)

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = next((proj for proj in projects if proj["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)

@app.route("/resume")
def resume():
    return render_template("resume.html")

# --- Flask-Mail configuration ---
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD
)
mail = Mail(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # --- Send email ---
        msg = Message("New Contact Form Message",
                      sender=email,  # user's email from form
                      recipients=[MAIL_USERNAME])  # your email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        flash("Your message has been sent successfully!", "success")
        return redirect('/contact')

    return render_template('contact.html')

# === Main ===
if __name__ == "__main__":
    app.run(debug=True)
