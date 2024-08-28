from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def get_summary_length(num_words):
    """Determine the summary length based on the number of input words."""
    if 100 <= num_words <= 500:
        return (50, 75)
    elif 500 < num_words <= 1000:
        return (75, 100)
    elif 1000 < num_words <= 1500:
        return (100, 135)
    elif 1500 < num_words <= 2000:
        return (135, 175)
    elif 2000 < num_words <= 2500:
        return (175, 225)
    elif 2500 < num_words <= 3000:
        return (225, 275)
    elif 3000 < num_words <= 3500:
        return (275, 325)
    elif 3500 < num_words <= 4000:
        return (325, 375)
    elif 4000 < num_words <= 4500:
        return (375, 425)
    elif 4500 < num_words <= 5000:
        return (425, 500)
    else:
        return (50, 75)  # Default if out of range

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    error = None

    if request.method == 'POST':
        text = request.form.get('input_text', '')
        file = request.files.get('file')

        if 'clear' in request.form:
            return render_template('index.html', summary=None, error=None)
        
        if text:
            try:
                # Count words in the input text
                num_words = len(text.split())
                min_length, max_length = get_summary_length(num_words)

                if num_words > 5000:
                    error = "Text exceeds the maximum limit of 5000 words."
                else:
                    # Summarize the text
                    summary_text = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
                    summary = summary_text[0]['summary_text']
            except Exception as e:
                error = f"An error occurred: {e}"
        
        elif file:
            try:
                # Handle file upload
                file_text = file.read().decode('utf-8')
                num_words = len(file_text.split())
                min_length, max_length = get_summary_length(num_words)

                if num_words > 5000:
                    error = "Text in file exceeds the maximum limit of 5000 words."
                else:
                    summary_text = summarizer(file_text, max_length=max_length, min_length=min_length, do_sample=False)
                    summary = summary_text[0]['summary_text']
            except Exception as e:
                error = f"An error occurred: {e}"

    return render_template('index.html', summary=summary, error=error)

if __name__ == '__main__':
    app.run(debug=True)
