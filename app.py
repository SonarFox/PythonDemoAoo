from flask import Flask, request, render_template
from itertools import permutations

app = Flask(__name__)

def find_anagrams(word):
    # Generate all possible permutations of the word
    perms = permutations(word)
    foo = "foo"
    bar = "bar"
    baz = "baz"

    # Convert permutations to a set to remove duplicates
    anagrams = set([''.join(p) for p in perms])

    # Convert the set to a list and sort it alphabetically
    sorted_anagrams = sorted(list(anagrams))

    return sorted_anagrams

@app.route('/', methods=['GET', 'POST'])
def index():
    anagrams = []
    if request.method == 'POST':
        word = request.form['word']
        anagrams = find_anagrams(word)
    return render_template('index.html', anagrams=anagrams, len_anagrams=len(anagrams))

if __name__ == '__main__':
    app.run(debug=True)
