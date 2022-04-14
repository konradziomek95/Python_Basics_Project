from flask import Flask, request

app = Flask(__name__)

FRONT_WEB = """
<head>
    <title>NUMBINATOR</title>
</head>
<body>
    <h1>Guess the number - Web game!</h1>
    <h2>Think about nuber between 1 and 1000</h2>
    <hr />
    <h2>Your nuber is {guess}</h2>
    <form action="/" method="POST">
        <input type="submit" name="user_answer" value="too big">
        <input type="submit" name="user_answer" value="too small">
        <input type="submit" name="user_answer" value="you won">
        <input type="hidden" name="min" value="{min}">
        <input type="hidden" name="max" value="{max}">
        <input type="hidden" name="guess" value="{guess}">
    </form>
</body>"""


@app.route('/', methods=['GET', 'POST'])
def guess():
    if request.method == "GET":
        return FRONT_WEB.format(guess=500, min=0, max=1000)
    else:
        guess = int(request.form.get("guess"))
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return "I win!"
        guess = (max_number - min_number) // 2 + min_number

        return FRONT_WEB.format(guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
