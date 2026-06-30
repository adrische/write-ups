# write-ups

A place to collect write-ups, notes, and tutorials.

*Contents*

* [Machine learning](#machine-learning)
* [Actuarial](#actuarial)
* [Other](#other)

## Machine learning

[Fast vector addition on A100 - 80 GB](https://github.com/adrische/learn-cuda/tree/main/Own-Kernels/GPUMODE)

My solution to the [GPU Mode leaderboard for vector addition](https://www.gpumode.com/leaderboard/543?tab=rankings). Is based on interpreting 8 float16 as 4 float32 (or one float4, to be precise) to saturate memory bandwidth, doing the calculations using the half2 vector type to maximize arithmetic efficiency, and finding the fastest load / store operations, and the finding best launch configuration. At time of writing this approach was listed at 6th place (tied with places 6-9), and I have run out of ideas what to try. The currently best solution is 0.27% (2.4 μs) faster.

----

#### [Don't install legacy Nvidia Software](Dont-install-legacy-Nvidia-software.md)

I have a Nvidia GeForce GTX 1050 Ti which is based on the Pascal architecture that is no longer supported by Nvidia. For example, the up to date version of Nsight Compute is not working for it. So I tried to install an older version of Nsight Compute that still supports my card. This brought an entire rat's tail of required downgrades of dependent software with it.
Depending on how you value your time, consider getting a GPU that's still supported.

----

#### Some more thoughts on debugging RL implementations

Recently, I have tried to implemented a number of RL algorithms such as [PPO](https://github.com/adrische/Reimplementing-PPO) for Mujoco and reduced versions of [DQN](https://github.com/adrische/MuZero-MsPacman#dqn-notebook) for Pong and [MuZero](https://github.com/adrische/MuZero-MsPacman#muzero-notebook-for-cartpole) (only for CartPole...) and I wanted to share some impressions from debugging these implementations. Many points have already been written up in other posts (see some links below), so I'll focus on what I found most important.

The full post is on [Reddit](https://www.reddit.com/r/reinforcementlearning/comments/1sgnz5m/some_more_thoughts_on_debugging_rl_implementations/)

----

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



----

## Other

[How to write a CV in the age of AI](How%20to%20write%20a%20CV%20in%20the%20age%20of%20AI.md)

I describe a workflow with Claude Projects how to automatically generate a CV and motivation letter that are targeted at a specific job opening. Note: I don't actually recommend following this approach. The background is that I worked on a project to automate this process and found this essentially trivial workflow achieving what I wanted.

----

[On working 80%](on-working-80%25.md)

A year ago, I decided to reduce my employment level from 100% to 80% and to take Fridays off.

My main motivation was to have some time for myself: Relax, reduce my stress level from work, have more time for side projects, do more sports, and maybe spend more time with my wife without the kids. This was only partially successful as there were a few things I had not realized beforehand. 

I’d like to describe my experience, and will focus on the effects this change had on my work, financial situation, side projects, and personal life / health.

----

[Lessons learned from designing and running a technical data science mentoring program](https://github.com/adrische/write-ups/blob/main/Data%20science%20mentorship%20program.md)

I recently organized a data science mentorship program at my organization. I realized there are lots of resources available on career mentoring, some of which are applicable to technical skills mentoring, but not all. I did find a few resources specifically related to data science mentoring, but there do not seem to be too many resources available yet, which is why I'm sharing my experiences here.

The article follows the structure of the program, with a focus on how I approached each step, and what could be done differently next time.
