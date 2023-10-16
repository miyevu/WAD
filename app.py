from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fizzbuzz')
def fizzbuzz():
    numbers = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("FizzBuzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(i)
    
    return render_template('fizzbuzz.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
