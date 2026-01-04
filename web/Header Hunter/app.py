from flask import Flask, request
import os

app = Flask(__name__)
FLAG = os.getenv('FLAG', 'csictf{h34d3rs_c4n_b3_sp00f3d}')

@app.route('/')
def index():
    admin_token = request.headers.get('X-Admin-Token')
    user_agent = request.headers.get('User-Agent')

    if admin_token == 'secret_admin_token_2024' and user_agent == 'AdminApp/1.0':
        return f'''
            <html>
                <body>
                    <h1>Admin Access Granted!</h1>
                    <p>Flag: {FLAG}</p>
                </body>
            </html>
        '''
    else:
        hint = ""
        if not admin_token:
            hint += "<li>Missing X-Admin-Token header</li>"
        elif admin_token != 'secret_admin_token_2024':
            hint += "<li>Invalid X-Admin-Token header</li>"

        if not user_agent or user_agent != 'AdminApp/1.0':
            hint += "<li>Invalid User-Agent</li>"

        return f'''
            <html>
                <body>
                    <h1>Access Denied</h1>
                    <p>This endpoint is only accessible from the admin application.</p>
                    <p>Hints:</p>
                    <ul>
                        {hint if hint else "<li>Check your headers...</li>"}
                    </ul>
                </body>
            </html>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
