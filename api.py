from flask import Flask, request, jsonify
import vectordb  # Import the functions from your vectordb.py file

app = Flask(__name__)
embeddings = vectordb.initialize_models_and_embeddings()
document_path = ""  # specify your document path here
retriever = vectordb.initialize_vector_store(embeddings, document_path)

@app.route('/retrieve', methods=['POST'])
def retrieve():
    data = request.get_json()  # Get JSON data from the request
    query = data['text']  # Get the text field from the data

    # Call the retrieve_documents function
    documents = vectordb.retrieve_documents(query, retriever)

    return jsonify({'documents': documents})  # Return the documents as JSON

if __name__ == '__main__':
    app.run(port=5000, debug=True)