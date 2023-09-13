ENESCU MARIA 311CA

# Stegano Flask Web Application

This is a Flask web application for steganography, which allows users to encode secret messages into images and decode them back. The application uses the Stegano library for the steganography operations.

## Implementation

The web application is built using Flask. It provides several routes for different functionalities:

- `/main_encode`: Renders the encode.html template, which is the main page for encoding a secret message into an image.
- `/main_decode`: Renders the decode.html template, which is the main page for decoding a secret message from an image.
- `/encode`: Handles the encoding process. It accepts a file upload for the original image, a text message, and a new image file name. It performs the steganography encoding using the Stegano library.
- `/decode`: Handles the decoding process. It accepts a file upload for the image with the hidden message and uses the Stegano library to extract the secret message.
- `/download`: Handles the download of the encoded or decoded image file.

The main page is accessible through the `/index` and `/` routes and renders the main.html template.

## Libraries

- Flask: The Flask library provides the web framework for building the web application.
- Stegano: The Stegano library is used for steganography operations, such as encoding and decoding secret messages into images.
- PIL: The Python Imaging Library (PIL) is used for image manipulation, such as extracting pixels and modifying images.

## Challenges Faced

During the implementation of this project, some challenges were encountered:

- File Validation: Validating the file types for uploaded images and ensuring they meet the requirements for steganography operations.
- User Input Handling: Handling user input, such as validating message length, new image file name, and ensuring proper encoding and decoding processes.
- Web UI Design: Creating an intuitive and user-friendly web interface for uploading images, entering messages, and displaying the results.

