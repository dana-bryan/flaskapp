from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

celeb_list = convert_to_dict('celebrity_youtubers.csv')

#make a list of pairs for the index.html template
pairs_list = []
for celeb in celeb_list:
    pairs_list.append(  (celeb['ID'], celeb['Celebrity'] ))


@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/celebrity/<num>')
def celebrity(num):
    celeb = celeb_list[int(num) - 1 ]
    return render_template('celeb.html', celeb=celeb)

if __name__ == '__main__':
    app.run(debug=True)
