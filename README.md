# write-ups

A place to collect write-ups, notes, and tutorials.

## Machine learning


#### Textcomparison

This is a web app to calculate different metrics to compare two texts.

You can compare two texts at the character-level (Levenshtein distance), word-level (BLEU score), or with a metric that respects the meaning (BERTScore using embeddings). 
You can also ask a language model to compare the two texts (this requires a valid OpenAI API key). 

The website is available at <a href="http://textcomparison.pythonanywhere.com" target="_blank">textcomparison.pythonanywhere.com</a> (it may take some time to load),
and the repository is available [here](https://github.com/adrische/textcomparison).

----

[A simple two-layer feed forward network with manual backpropagation](manual-backpropagation-example.py)

This is a short expository Python code of a tiny neural net, written from scratch in Numpy with manual backpropagation. We then verify gradients with Pytorch.

----

[Ask questions to your PDF documents - a tutorial](Ask%20questions%20to%20your%20PDF%20documents%20-%20a%20tutorial.ipynb)

In this notebook, we use a large language model to ask and answer questions to PDF documents. You may want to do this with non-publically available documents, or with documents that appeared after the language model was trained.

Additionally, we want to do run the language model locally. This has advantages for privacy and confidentiality (if you cannot send your data to a remote service).

We will use Llama 7B as the language model, and langchain for integration of the other necessary pieces.

----

[Machine learning model validation](machine-learning-model-validation.md)

The use of machine learning models quickly expands to business areas with strong regulation, such as finance and medicine. Machine learning models and their validation differ substantially from classical models and classical model validation. Regulators, model validation teams and model developers need to adjust to different requirements on model validation and model development.

These notes aim to go into detail what topics model validation of machine learning models should address.




----

## Actuarial

[A tiny introduction to a Poisson Generalized Linear Model (GLM), spelled-out in code](GLM.pdf)

This is an introduction to a very simple example of a Poisson GLM in R. The goal is that we understand and manually implement all output of `summary()` for this special case. This includes:

* how the GLM is fitted to the data,
* how to predict from the GLM,
* how categorical vs. numerical variables influence the fit,
* the derivation and interpretation of quality of fit indicators (deviance and AIC),
* one possibility to test for statistical significance of including an additional parameter in the model (likelihood ratio test),
* the meaning and derivation of parameter standard errors and p-values.

The emphasis is on the expositional code, rather than on mathematical derivations or intuition for the quantities introduced.

The [R Code](GLM.Rmd) is also available.

----

[Slides of actuarial colloqium](https://github.com/adrische/actuary/blob/master/colloquium/Adrian%20Scheerer%20SAV%20Kolloquium%20Presentation.pdf)

These are the slides (in German) that I prepared for the last exam (colloquium) to become an actuary (member of Swiss Association of Actuaries, SAV). The topic was _Steigende Teuerungsraten: Chancen und Risiken im Reserving und Risk Management aus aktuarieller Sicht_, which roughly translates as _Rising inflation rates: opportunities and risks in reserving and risk management from an actuarial perspective_. The slides are also available in the [collection of colloquium slides](https://www.actuaries.ch/de/fach-arbeitsgruppen/junge-aktuare/pruefungskolloquium) by the SAV young actuaries.

----

[Least-Squares Monte-Carlo for an American Put Option](Least-Squares-Monte-Carlo-American-Put.pdf)

These notes reproduce the first example on least-squares Monte-Carlo from paper _Valuing American Options by Simulation: A Simple Least-Squares Approach_ by Longstaff and Schwartz, [available here](https://people.math.ethz.ch/~hjfurrer/teaching/LongstaffSchwartzAmericanOptionsLeastSquareMonteCarlo.pdf).

The [R Code](Least-Squares-Monte-Carlo-American-Put.Rmd) is also available.

----

[Proof of Thieles Differential Equation](https://github.com/adrische/actuary/blob/master/selected-topics-in-life-insurance/Thieles-Differential-Equation.pdf)

We prove Thiele's differential equation in continuous time from scratch (ignoring some technical details). This write-up tries to spell out all steps in the derivation of this equation, following M. Koller's lecture notes on "Selected Topics in Life Insurance" (not publicly available).
