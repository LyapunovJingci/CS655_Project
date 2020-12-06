from flask import Flask, request
import json
from face_compare import compare_faces

app = Flask(__name__)

@app.route('/face_match'), methods=['POST']
def face_match():
	if request.method = 'POST'
		if ('file1' in request.files) and ('file2' in request.files)
			file1 = requests.files.get('file1')
			file2 = requests.files.get('file2')
			result = compare_faces(file1, file2)
			response_data = {"match": bool(result)}
			return json.dumps(response_data)
app.run(host='0,0,0,0', port='5001', debug=True)