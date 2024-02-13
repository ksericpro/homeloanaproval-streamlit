# Why should data scientists use Streamlit?

The best thing about Streamlit is that you don't even need to know the basics of web development to get started or to create your first web application. So if you're somebody who's into data science and you want to deploy your models easily, quickly, and with only a few lines of code, Streamlit is a good fit.

One of the important aspects of making an application successful is to deliver it with an effective and intuitive user interface. Many of the modern data-heavy apps face the challenge of building an effective user interface quickly, without taking complicated steps. Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time.

Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application:

No front-end (html, js, css) experience or knowledge is required.
You don't need to spend days or months to create a web app, you can create a really beautiful machine learning or data science app in only a few hours or even minutes.
It is compatible with the majority of Python libraries (e.g. pandas, matplotlib, seaborn, plotly, Keras, PyTorch, SymPy(latex)).
Less code is needed to create amazing web apps.
Data caching simplifies and speeds up computation pipelines.

# Setup

## install dependencies
- pip install matplotlib
- pip install scikit-learn==1.2.2

## run
- streamlit run homeloanapproval-ui.py

# Deploy to streamlit cloud
- pip freeze > requirements.txt
- git add .
- git commit -m "requirements.txt"
- git push

# url
- [link] (https://homeloanaproval-app-tj8m5tymqnvogsqfxwuxil.streamlit.app/)

# References

- [Link] (https://www.datacamp.com/tutorial/streamlit)
- [Dataset] (https://www.kaggle.com/datasets/rishikeshkonapure/home-loan-approval)
- [Prediction] (https://www.kaggle.com/code/srikanth917/home-loan-approval-prediction)
- [Saving Model] (https://practicaldatascience.co.uk/machine-learning/how-to-save-and-load-machine-learning-models-using-pickle#:~:text=Save%20the%20model%20with%20Pickle,pkl%20.)