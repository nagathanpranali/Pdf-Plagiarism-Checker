PDF Plagiarism Checker App

A web application that compares two PDF documents and detects plagiarism using text similarity techniques.
 
Check out the live website https://pdf-plagiarism-checker.onrender.com/

Features
* Upload two PDF files for comparison
* Automatic text extraction from PDFs
* Calculates similarity using cosine similarity
* Displays plagiarism level:
    * Highly Plagiarised
    * Medium Plagiarised
    * Unique
* Simple and user-friendly interface

Tech Stack
* Python
* Flask
* PyMuPDF (fitz)
* Scikit-learn
* HTML, CSS

File Input Format
* Both uploaded files must be in PDF format
* Files should contain readable text (not scanned images)

How It Works
1. User uploads two PDF files
2. App validates file format (.pdf)
3. Extracts text from both PDFs using PyMuPDF
4. Converts text into vectors using CountVectorizer
5. Computes cosine similarity between documents
6. Calculates similarity score (in percentage)
7. Classifies result:
    * Score > 70 → Highly Plagiarised
    * Score > 40 → Medium Plagiarised
    * Otherwise → Unique
8. Displays the plagiarism result
