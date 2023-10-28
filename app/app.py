from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
        bg_color = "Lime"
        font_color = "white"
        return render_template('index.html', bg_color=bg_color, font_color=font_color)

if __name__ == '__main__':
        app.run(host="0.0.0.0",port="8080")
    #margin-top: -100px; 
    #margin-left: -900px; 
