from flask import *
import fitz
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
	if request.method == "POST":
		#files
		f1 = request.files["f1"]
		f2 = request.files["f2"]

		#check both are ending .pdf
		if not f1.filename.lower().endswith(".pdf"):
			msg = "first file should be pdf"
			return render_template("home.html", msg=msg)

		if not f2.filename.lower().endswith(".pdf"):
			msg = "second file should be pdf"
			return render_template("home.html", msg=msg)

		#save files
		f1.save("a.pdf")
		f2.save("b.pdf")

		#read the content
		f1 = fitz.open("a.pdf")
		s1 = ""
		for f in f1:
			s1 = s1 + f.get_text()
		f1.close()

		f2 = fitz.open("b.pdf")
		s2 = ""
		for f in f2:
			s2 = s2 + f.get_text()
		f2.close()

		#vectorize
		texts = [s1.strip(), s2.strip()]
		cv = CountVectorizer()
		vector = cv.fit_transform(texts)
	
		#cs
		cs = cosine_similarity(vector)
		score = round(cs[0][1] * 100,2)
		#msg = "Similarity score = " + str(score)
		if score > 70:
			msg = "Highly Plagiarised"
		elif score > 40:
			msg = "Medium Plagiarised"
		else:
			msg = "Unique"
		return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")

#app.run(debug=True, use_reloader=True)

