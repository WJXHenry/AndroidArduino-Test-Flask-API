from flask import Flask, request
import os

app = Flask(__name__)

FILE_KEY = 'unsent_data' # This is the key to the file you want to read

@app.route('/sendFile', methods=['POST'])
def sendFile():
    file = request.files[FILE_KEY] # Throws a KeyError if the sent file's key is not FILE_KEY
    contents = file.read()
    print("Read:\n\n" + contents + "\nEnd\n")
    print("Writing to file...")
    if not os.path.exists('./uploads'):
        os.makedirs('uploads')
    with open("./uploads/uploaded-file.csv", "wb") as fo:
        fo.write(contents)
    print("Done.\n")
    return "Got data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)