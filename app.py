from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_navigation():
    return {
        'site_name': 'Erasmus Guide',
        'navigation': [
            {'label': 'Home', 'endpoint': 'home'},
            {'label': 'About Us', 'endpoint': 'about'},
            {'label': 'Consulting', 'endpoint': 'consulting'},
            {'label': 'Opportunities', 'endpoint': 'opportunities'},
            {'label': 'Blog', 'endpoint': 'blog'},
            {'label': 'Contact', 'endpoint': 'contact'},
        ],
    }

@app.route('/')
def home():
    highlights = [
        {'title': 'Program guidance', 'description': 'Find the right Erasmus track, partner university, and study plan.'},
        {'title': 'Application advice', 'description': 'Prepare documents, adapt your motivation letter and get deadline reminders.'},
        {'title': 'Life abroad tips', 'description': 'Get resources on housing, travel, local culture and academic success.'},
    ]
    return render_template('index.html', highlights=highlights)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/consulting')
def consulting():
    services = [
        {'title': 'University selection', 'description': 'Compare host institutions, academic fits and Erasmus agreements.'},
        {'title': 'Credit transfer support', 'description': 'Plan your course load so credits transfer cleanly back home.'},
        {'title': 'Application checklist', 'description': 'Follow a clear list of required forms, deadlines and eligibility steps.'},
    ]
    return render_template('consulting.html', services=services)

@app.route('/opportunities')
def opportunities():
    opportunities = [
        {'title': 'Erasmus+ semesters', 'detail': 'Study at a partner institution for one or two academic semesters.'},
        {'title': 'Summer schools', 'detail': 'Short-term academic courses with cultural activities across Europe.'},
        {'title': 'Research placements', 'detail': 'Work on a research project while earning academic credit abroad.'},
    ]
    return render_template('opportunities.html', opportunities=opportunities)

@app.route('/blog')
def blog():
    posts = [
        {
            'title': 'Preparing Your Erasmus Application',
            'summary': 'Essential tips on documents, motivation letters, and choosing the right courses.',
            'date': 'May 2026',
        },
        {
            'title': 'Top Destinations for Erasmus Students',
            'summary': 'A quick overview of popular Erasmus cities with strong academic programs.',
            'date': 'April 2026',
        },
        {
            'title': 'How to Handle Credit Transfer',
            'summary': 'Understand the key steps to ensure your credits count toward graduation.',
            'date': 'March 2026',
        },
    ]
    return render_template('blog.html', posts=posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
