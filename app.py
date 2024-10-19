from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Preetham Rodriguez"
    
    username = os.environ.get('USER', 'Unknown')
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except subprocess.CalledProcessError:
        top_output = "Unable to fetch top output"
    
    html_content = f"""
    <html>
    <body>
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    
    return html_content

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
