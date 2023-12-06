# auto git pull implementation

from flask import Flask, request, jsonify
import subprocess
# initialize flask instance
app = Flask(__name__)

@app.route('/pullwebhook', methods=['POST'])
def git_webhooks():
    try:
        payload = request.json
        branch = payload['ref'].split('/')[-1]

        if branch == 'main':
            repo_path = '/path/to/your/repo'
            subprocess.run(['git', '-C', repo_path, 'pull', 'origin', branch])
            return jsonify({'status': 'success', 'message': 'Git pull completed.'}), 200
        else:
            return jsonify({'status': 'ignored', 'message': 'request of Push event for a different branch.'}), 200
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500



if __name__ == '__main__':
    app.run()