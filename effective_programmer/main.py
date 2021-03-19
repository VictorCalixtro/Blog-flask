from flask import Flask, render_template

#Flask uses the name arguement to determine the location of the application, which allows to locate other files such as images and templates
app = Flask(__name__)

#Clients such as web browsers send requests to the web server, flak needs to know what code to run for each url request
#So that keeps a mapping of urls to python functions. The association between a url and the function that handles it is called a 
#Route

#Most convenient way to define a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
def topics():
    return render_template('topics.html')

@app.route('/about')
def about():
    return render_template('about.html')

#Fields begin here

#index fields

@app.route('/complexity_analysis')
def complexity_analysis():
    return render_template('/Complexity.html')


@app.route('/neovim')
def neovim():
    return render_template('/01_NeoVim.html')

@app.route('/fractals')
def fractals():
    return render_template('/fractals.html')

@app.route('/Maze-Runner')
def maze_runner():
    return render_template('/Maze-Runner.html')

@app.route('/shpe')
def shpe():
    return render_template('/shpe.html')

#topic fields

@app.route('/algorithms')
def algorithms():
    return render_template('/algorithms.html')

@app.route('/Apps')
def Apps():
    return render_template('/Apps.html')



if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
