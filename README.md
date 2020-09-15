# Sentiment-analysis-of-code-mixed-text

As the range of internet grows a lot of code-mixed data is generated from the users of the multilingual society. One of the common practice is using Hindi language words written with the help of the English alphabets. The project implements an LSTM model for the sentiment analysis of Hindi-English (Hi-En) code-mixed data and comparing it with the pre-existing character- level LSTM model.

The project focuses on learning the sentiments of individual words and combining them all together to determine the sentiment of the whole sentence. The learning model comprises of word-level LSTM architecture instead of character-level representations. This linguistics prior to the architecture enables us to learn the information about the sentiment value of important morphemes. Data translation and then pre-trained GloVe Embedding is used to preprocess the code-mixed dataset. The processed data is used to train a multilayer LSTM classifier to determine the sentiments of the text. The performance of the trained model is compared with that of character-level architecture. The system attains a performance comparable to that of the existing architecture and outperforms the available system in classifying some examples of the code-mixed dataset.

## About the Repository

This Repository contains Dataset, Trained Model, Reports, Presentation, etc related to the project. A brief description of various files present in this repo:

    1. Project_Report.pdf         -->   It is a 50+ Page Report that describes the complete Project.

    2. Project_Presentation.ppt   -->   It is a PowerPoint Presentation to have a better understanding of the Project.

    3. Steps_of_Execution.pdf     -->   It is a detailed description of how to extract and use the trained model over actual test data.

    4. Test_Data.h5               -->   It contains the Test Embedding Vectors for testing of the trained model.

    5. LSTM_Keras_model.h5        -->   This file contains the trained model in .h5 format.

    6. code_mixed_basic.py        -->   Python file that contains the Source code on which the model is trained.

    7. Code_Mixed_Basic.ipynb     -->   IPython Notebook file that also contains the same python Source code in a much interactive manner.

    8. translated_data.txt        -->   This file contains the Translated words generated using Google Translation API.

    9. testing.py                 -->   This python file contains the code for visualizing model, data and also test the model over actual testing data.




## Note: Star the Repository if someone clones it or forks it.
