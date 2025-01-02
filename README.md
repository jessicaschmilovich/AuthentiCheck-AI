# AuthentiCheck AI

AuthentiCheck AI is an advanced web platform designed to empower users, particularly teenagers, to identify false AI-generated content in texts, images, and voices. By leveraging machine learning and custom models, the platform enhances digital literacy and promotes responsible online engagement by providing percentage likelihoods of AI generation. HTML structures the interface for the image and voice detectors, while Python is used for the text detector, with ReScript and Nix supporting text-related functionality and backend processes. This project earned me recognition as an International Semifinalist in the 2024 Technovation Girls Challenge.

**Features:**

1. Image Detection  
   Analyzes images and provides a percentage likelihood of them being AI-generated.

2. Text Detection  
   Evaluates text for AI-generated characteristics and delivers a percentage likelihood through an interactive Replit webpage linked to the main platform.

3. Voice Detection  
   Analyzes voice samples and offers a percentage likelihood of AI generation based on acoustic and syntactic features.

**Project Structure:**

image_detector/  
Contains resources for detecting AI-generated images. 
- ml_image_detection.html: Handles analyzing and identifying AI-generated image samples.

text_detector/  
Handles the detection of AI-generated text using custom ML models.  
- main.py: Entry point for running text detection.  
- mlmodel.py: Core logic for text analysis and model interaction.  
- mltext.py: Contains helper functions for preprocessing text data.  
- poetry.lock and pyproject.toml: Manage project dependencies using the Poetry package manager.  
- replit.nix: Configuration file for Replit development environment.  
- temp.txt: Temporary data storage for model outputs.  
- pycache/: Directory for cached Python bytecode files.

voice_detector/  
Contains resources for detecting AI-generated voices.
- ml_voice_detection.html: Handles analyzing and identifying AI-generated voice samples.
