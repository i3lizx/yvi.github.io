from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        try:
            youtube_link = request.form['youtube_link']
            yt = YouTube(youtube_link)
            stream = yt.streams.first()
            stream.download()
            return redirect('/')
        except:
            return 'Error'
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
