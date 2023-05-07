from flask import Flask, render_template
import requests

animals = [
            {"letter": "A", "link": "https://media.giphy.com/media/8shyTgbZKKLzW/giphy.gif"},
            {"letter": "B", "link": "https://media.giphy.com/media/nFfThe8MvKSI0/giphy.gif"},
            ]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", animali=animals, id=0)


@app.route("/animal/<index>")
def show_animal(index):
    requested_animal = None
    print(index)
    for animal in animals:
        if animal["letter"] == index:
            print(animal["letter"])
            requested_animal = animal
            print(animal)
    return render_template("animal.html", animale=requested_animal)



if __name__ == "__main__":
    app.run(debug=True)
