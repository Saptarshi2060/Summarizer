# Text Summarizer

## Overview

The Text Summarizer application is a web-based tool designed to generate concise summaries from longer texts. It allows users to input or upload text and receive a summary that highlights the key points. The application dynamically adjusts the summary length based on the size of the input text, providing a tailored summarization experience.

## Features

- **Text Input and Upload:** Enter text directly or upload a file containing the text.
- **Dynamic Summary Length:** Adjusts the length of the summary based on the input text size.
- **Error Handling:** Displays errors for texts exceeding the maximum word limit or other issues.
- **Clear Button:** Allows users to reset the input and output fields.

## Requirements

- Python 3.7 or higher
- Flask
- Transformers library from Hugging Face

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer
