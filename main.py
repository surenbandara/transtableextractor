from flask import Flask, request, jsonify
import io
from extractor import main

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})
        

        pdf_bytes = file.read()
        table_data = main("Pathum" , pdf_bytes )
        # Return the extracted table data as JSON response
        return jsonify({"table_data": table_data})

        # try:
        #     #Extract table data from the uploaded PDF file
          
        #     pdf_bytes = file.read()
        #     table_data = main("Pathum" , pdf_bytes )
        #     # Return the extracted table data as JSON response
        #     return jsonify({"table_data": table_data})

        # except Exception as e:
        #     return jsonify({"error": str(e)})

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)


