# MiniRetrieve: Text Retrieval API
MiniRetrieve is a simple Python program built with langchain that retrieves text from documents via an API.

## Installation
To install the dependencies of MiniRetrieve, you will need Python and pip installed on your system. If you don't have them already, you can download Python here and pip will be installed with it.

1. Clone the repository:
```
$ git clone https://github.com/your_github_username/MiniRetrieve.git
$ cd MiniRetrieve
```

2. Create a virtual environment (optional, but recommended):
```
$ python3 -m venv env
$ source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
3. Install requirements using pip:
```
$ pip install -r requirements.txt
```
4. Add your openai key to the vectordb.py file OR from the command line:
ubuntu:
```
export OPENAI_API_KEY="your_key"
```
windows powershell:
```
$env:OPENAI_API_KEY="your_key_here"
```
windows command prompt:
```
set OPENAI_API_KEY=your_key_here
```

# Usage
## Load a File

Before you start the Flask app, you should specify the path to the document from which you want to retrieve text. You can do this in the vectordb.py file, specifically in this line:

```
document_path = "path/to/your/document.pdf"  # specify your document path here
```

## Start the Flask app

Once you have loaded your file correctly, you can start the Flask app which will initialize everything and start the server:
```
$ python api.py
```

This will start the Flask server on port 5000.

## Make a Call to the API

To retrieve text from your documents, you need to make a POST request to the **'/retrieve'** endpoint. The request should contain a JSON body with a text field which is the query you're submitting to the **'text'** retrieval function.

Here's an example with curl:
```
$ curl -X POST -H "Content-Type: application/json" -d '{"text":"What is abductive reasoning?"}' http://localhost:5000/retrieve
```
The API will return a JSON object with a documents field that contains the retrieved text as a single string.

## Here are the instructions for using Postman to test the /retrieve endpoint:

1. Open Postman. If you do not have Postman installed, you can download it here.

2. Click on the + button to create a new tab for a new request.

3. In the new tab, from the dropdown menu on the left, select POST as the request type.

4. Enter the URL for your local server into the URL field, which should be http://localhost:5000/retrieve if the server is running locally on port 5000.

5. Below the URL field, go to the Body tab.

6. Select the raw option, and then from the dropdown menu on the right, select JSON.

7. In the text field that appears, input your JSON. For your case, it would be something like:
```
{
    "text":"What is abductive reasoning?"
}
```
After everything is set, click the **Send** button to make the request.

The returned JSON will appear in the lower panel. You should see a key named "documents" with the corresponding contents fetched by the retriever as its value.

Remember to start your Flask application before making the API request.

# Notes
Please note that MiniRetrieve is designed to be very minimal and simple. If you need to perform more complex operations with langchain or perform more custom retrievals, you'll need to modify the provided scripts or use more advanced features from langchain.

Additionally, be sure to handle exceptions and edge cases in your production setting. For instance, think about what should happen if the provided document path is invalid, or if the text retrieval failed for some reason. MiniRetrieve does not currently handle these exceptions.
