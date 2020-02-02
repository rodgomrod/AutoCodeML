import os
import subprocess
import sys
import platform

from flask import Flask, render_template, request

dirname, filename = os.path.split(os.path.abspath(__file__))
dirname = '/'.join(dirname.split('/')[:-1])

app = Flask(__name__)

## Operating System ##
system = platform.system()
if system == 'Windows':
    interpreter = 'python'
else:
    interpreter = 'python3'

def run_main(dict_result):
   os.system('{0} main.py {1} {2} {3} {4} {5} {6} {7} "{8}" {9} {10} {11} {12} {13} {14}'.format(
      interpreter,
      dict_result["file_name"],
      dict_result["data_path"],
      dict_result["separate"],
      dict_result["how_cat"],
      dict_result["how_num"],
      dict_result["how_ft_sel"],
      dict_result["mode"],
      dict_result["params"],
      dict_result["alg"],
      dict_result["how_val"],
      dict_result["train_path"],
      dict_result["test_path"],
      dict_result["target_label"],
      dict_result["drop_cols"]
   ))

@app.route('/')
def student():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        dict_result = dict(result)
        if dict_result['separate'] != 'True':
            dict_result['separate'] = 'False'
        run_main(dict_result)
        return render_template('result.html',
                               result=result)


if __name__ == '__main__':
    url = "http://localhost:5000"
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            print('Please open a browser on: ' + url)

    app.run(debug=True)
