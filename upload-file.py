from flask import Flask, request

app = Flask(__name__)

@app.route('/sendFile', methods=['POST'])
def sendFile():
    file = request.files['unsent_data']
    contents = file.read()
    print("Read:\n\n" + contents + "\nEnd\n")
    print("Writing to file...")
    with open("uploaded-file.csv", "wb") as fo:
        fo.write(contents)
    print("Done.\n")
    return "Got data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)