from flask import render_template
from app import main_bp

@main_bp.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@main_bp.route('/about')
def about():
    """About page route"""
    return render_template('about.html')




from flask import render_template, current_app
app.register_blueprint(main_bp)

app = create_app()

@app.route('/')
def index():
    """Render the main application page"""
    csrf_token = app.security_manager.generate_csrf_token()
    return render_template('index.html', csrf_token=csrf_token)

@app.route('/image-to-3d')
def image_to_3d():
    """Render the image to 3D conversion page"""
    csrf_token = app.security_manager.generate_csrf_token()
    return render_template('image_to_3d/upload.html', csrf_token=csrf_token)

@app.route('/my-models')
def my_models():
    """Render the user's models page"""
    csrf_token = app.security_manager.generate_csrf_token()
    return render_template('my_models.html', csrf_token=csrf_token)

@app.route('/chat')
def chat():
    """Render the customer support chat page"""
    csrf_token = app.security_manager.generate_csrf_token()
    return render_template('chat.html', csrf_token=csrf_token)