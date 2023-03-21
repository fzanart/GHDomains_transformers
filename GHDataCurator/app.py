from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from github import Github
import csv

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    # Get form data
    token = request.form['token']
    repos = request.form['repos']

    if not token:
        flash('You need to provide a GitHub token. We do not store this information.')
    if not repos:
        flash('You need to provide a GitHub repository, please enter one or more comma separated GitHub repositories.')

    return redirect(url_for('index'))

    data_type = request.form['data']
    
    # # Connect to GitHub API
    # g = Github(token)
    
    # # Loop through selected repos and get data
    # data = []
    # for repo in repos.split(','):
    #     r = g.get_repo(repo.strip())
        
    #     if data_type == 'readme':
    #         data.append(r.get_readme().decoded_content)
    #     elif data_type == 'license':
    #         data.append(r.get_license().decoded_content)
    #     elif data_type == 'description':
    #         data.append(r.description)
    #     elif data_type == 'languages':
    #         data.append(r.get_languages())
    
    # # Write data to CSV file
    # with open('data.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for row in data:
    #         writer.writerow([row])
    
    # # Send file to user
    # return send_file('data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
