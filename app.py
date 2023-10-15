from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def main_Menu():
    if request.method == "POST":
        import Backend
        button_clicked = request.form['submit_button']

        if button_clicked == "Lights On":
            Backend.lights_on()
        elif button_clicked == "Lights Off":
            Backend.lights_on()
        return render_template("Main Menu.html")
    else:
        return render_template("Main Menu.html")


if __name__ == '__main__':
    app.run()
