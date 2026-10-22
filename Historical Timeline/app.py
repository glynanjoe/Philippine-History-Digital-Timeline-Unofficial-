from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sources")
def sources():
    return render_template("sources.html")


@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/timeline/magellan")
def magellan_detail():
    return render_template("magellan_detail.html")

@app.route("/timeline/blood-compact")
def blood_compact_detail():
    return render_template("blood_compact_detail.html")

@app.route("/timeline/spanish-rule")
def spanish_rule_detail():
    return render_template("spanish_rule_detail.html")

@app.route("/timeline/manila")
def manila_detail():
    return render_template("manila_detail.html")

@app.route("/timeline/galleon-trade")
def galleon_detail():
    return render_template("galleon_detail.html")

@app.route("/timeline/cavite-mutiny")
def cavite_mutiny_detail():
    return render_template("cavite_mutiny_detail.html")

@app.route("/timeline/gomburza")
def gomburza_detail():
    return render_template("gomburza_detail.html")

@app.route("/timeline/katipunan")
def katipunan_detail():
    return render_template("katipunan_detail.html")

@app.route("/timeline/independence")
def independence_detail():
    return render_template("independence_detail.html")

@app.route("/timeline/first-republic")
def first_republic_detail():
    return render_template("first_republic_detail.html")

@app.route("/timeline/early-societies")
def early_societies_detail():
    return render_template("early_societies_detail.html")

@app.route("/timeline/japanese-occupation")
def japanese_occupation_detail():
    return render_template("japanese_occupation_detail.html")

@app.route("/timeline/independence-1946")
def independence_1946_detail():
    return render_template("independence_1946_detail.html")

@app.route("/timeline/edsa-people-power")
def edsa_detail():
    return render_template("edsa_detail.html")








if __name__ == "__main__":
    app.run(debug=True)