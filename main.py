from flask import Flask, request, jsonify
import io
from extractor import extractor

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})
        

        pdf_bytes = file.read()
        table_data = extractor(pdf_bytes )
        return jsonify({"table_data": table_data})
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)


