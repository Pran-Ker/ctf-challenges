from flask import Flask, request, make_response
import base64
import json
import os

app = Flask(__name__)
FLAG = os.getenv('FLAG', 'csictf{c00k13s_4r3_n0t_s3cur3}')

@app.route('/')
def index():
    cookie = request.cookies.get('session')

    if not cookie:
        # Create default guest session
        session_data = {"username": "guest", "role": "user"}
        encoded = base64.b64encode(json.dumps(session_data).encode()).decode()
        resp = make_response('''
            <html>
                <body>
                    <h1>Welcome Guest!</h1>
                    <p>You are logged in as a guest user.</p>
                    <p>Can you become an admin?</p>
                </body>
            </html>
        ''')
        resp.set_cookie('session', encoded)
        return resp

    # Decode session
    try:
        decoded = base64.b64decode(cookie).decode()
        session_data = json.loads(decoded)

        if session_data.get('role') == 'admin':
            return f'''
                <html>
                    <body>
                        <h1>Welcome Admin!</h1>
                        <p>Congratulations! Here's your flag: {FLAG}</p>
                    </body>
                </html>
            '''
        else:
            return f'''
                <html>
                    <body>
                        <h1>Welcome {session_data.get("username", "User")}!</h1>
                        <p>You are logged in as a {session_data.get("role", "user")}.</p>
                        <p>Can you become an admin?</p>
                    </body>
                </html>
            '''
    except:
        return "Invalid session cookie!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
