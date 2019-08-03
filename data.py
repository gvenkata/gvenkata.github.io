from flask import Flask,render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)
  
@app.route('/data')
def data_analysis():
	x = pd.DataFrame(np.random.randn(5, 6), columns=list('ABCDEF'))
	return render_template("data.html",  data=x.to_html())
 
if __name__ == '__main__':
    app.run(debug=True)