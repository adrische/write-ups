# Machine Learning Model Validation

The use of machine learning models quickly expands to business areas with strong regulation, such as finance and medicine.
Machine learning models and their validation differ substantially from classical models and classical model validation. 
Regulators, model validation teams and model developers need to adjust to different requirements on model validation and model development.

These notes aim to go into detail what topics model validation of machine learning models should address. 

The term _model validation_ is actually used in several contexts and can mean at least the following three things:

* **Model evaluation:** Estimating a model's performance,

* **Code and algorithm review:** Fixing technical and methodological bugs,

* **Regulatory model validation:** To be allowed to use the model in production.

We will focus on the latter two: How to prevent any errors from happening during model deployment, and how to ensure regulatory approval. Model evaluation will play an important role for both.



These notes are split in the following sections:

[**Data:**](#data) The central part of any machine learning model is the data that the model operates on, during training, testing, and deployment.

[**Design:**](#design) This section is centered around mathematical appropriateness of the chosen model approach.

[**Implementation:**](#implementation) This section highlights how errors could occur during the programming part of model development, and how to possibly avoid them.

[**Output:**](#output) This section is about verifying the model based on its outputs, a central way of validating any machine learning model.

[**Documentation:**](#documentation) Machine learning models have some special requirements on the documentation that differs from classical models.

[**Governance and Use:**](#governance-and-use) Questions around fulfillment of regulatory requirements and model usage.


----


**Disclaimer:**
These notes are my personal view and do not necessarily express the opinion of any of my current or former employers. I am not responsible for the content of external links.

If you have any questions, suggestions, other comments, or want to collaborate with me on topics around machine learning model validation please [reach out to me](mailto:adrianscheerer@gmail.com).

----

Version history:

* July 2020: initial version, comments welcome!


----


## Data

As machine learning models heavily rely on data, this section comes first.


### Data properties

Analyze the data set used with respect to the following properties.

**Representativeness:** Are the train and test data representative of all future use cases? Does the data span the desired input-output space? This is to ensure the model behavior is known on its intended domain and to prevent any generalization error.

**Data set shift:** Do train and test data have the same statistical properties, and the same properties as the data the model is operating on once in deployment? 

**Data bias:** Data can be biased in many ways. Bias is such an important topic in machine learning it would deserve its own chapter. Here, we restrict ourselves to a few examples to raise awareness of how bias may arise and influence machine learning models. Please consult additional resources on bias.

Examples of biased data are:

* In a hypothetical spam email identification model: All messages of a minority group are labeled as spam.
* The [tank vs. no tank classification problem](https://www.gwern.net/Tanks): All pictures in the training set were pictures of tanks at day. As a consequence, the model learned to distinguish day from night and all pictures that were taken at night, even if they contained tanks, were classified as not a tank.
* The [Dog vs. Husky classification problem](https://arxiv.org/abs/1602.04938): All pictures of huskies were taken in front of a snowy background. As a consequence, all pictures in front of snowy background were classified as huskies, even if they were pictures of dogs.
* Human bias: Assess to what extend humans have been part in data generating, data selection and the data labeling process and could have introduced bias.

**Skewed data:** Are test and training data for categorical features evenly distributed over the classes? If not, this could be a source of bias and the assumptions of some models on class balance might be violated.

**Data stability:** Is the proposed model stable when the data set is changing? This is important for example if the model will be retrained on new or updated data set during production. Assess the stability of the training data and resulting models in time.

**Outlier treatment:** How are outliers treated? If outliers have been removed from the training data, how can you ensure that the model works correctly once deployed? Outliers are likely to happen during production.


### Data preprocessing

During data preprocessing, modifications are made to the data that will influence model performance. Among others, data preprocessing includes modifications to the data itself, such as missing values imputation, data rescaling and feature engineering, but also to the way the data is presented, such as for example the way categorical variables are encoded.

The following points can be assessed during data preprocessing validation:

* Has there been data leakage, i.e., has information about test data been used during model training? For example, data leakage can happen during data preprocessing if statistical properties of the combined train and test set have been used during data normalization of the training set. 
* How have missing values been treated? For example, see how the model changes if N/A values are no longer replaced by the mean of a feature, but by a random sample from available values of the feature. Does the specific way missing values are replaced make sense from a business perspective?
* If feature selection is part of the model: What features have been selected? Is there a business explanation for why these exact features have been chosen? How do different features influence model performance? Are the features meaningful or are only spurious patterns selected?
* How is data with special properties handled, such as sparse data, wide data, or categorical features with many categories?
* Is the input data scaled to meet the assumptions of the model?
* Have train and test data been preprocessed the same way?
* How are individual input instances preprocessed when applying the model?


### Data privacy

Questions on data privacy and data licenses.

* If you use cloud-based model training or deployment: Does your institution’s privacy policy allow you to upload the data?
* Is the data anonymized?
* Are you obeying all licenses that are attached to your data?


### Data other

Other questions to ask.

* Is the data labeled correctly?
* Is the data appropriate and meaningful? For example, you would use balance sheet data to predict credit ratings, but not what is the favorite color of the employees.
* Is the data extensive? Has nothing been left out or forgotten during data collection?
* Are there logical errors or inconsistencies in the data? An example of inconsistent data would be that results of a poll show that 73% of the respondents consider option A, 78% consider option B, whereas 40% consider both options.
* Is the data real, as opposed to generated?
* The train-test split needs to respect whether several observations come from the same underlying source. For example, if several medical observations have been collected from the same patient, these observations should not occur in both train and test data.




## Design

This section is about the design of the model from an algorithmic and mathematical perspective.

* Algorithm: If the type of model is known (which might not be the case for example for closed third party models), you can ask the following questions: 
  * Is the algorithm appropriate from a methodological point of view? 
  * Are the assumptions on the data met? Possible requirements might be that a variable is normally distributed or that different variables need to be similar order of magnitude. 
  * Is the model adapted to the intended use case? 
* Metric: Is the target metric really the most relevant metric possible for the problem? For example, accuracy is not a meaningful evaluation metric if the data is very imbalanced.
* Overfitting: Has the problem of overfitting been avoided or addressed? [There are many ways of overfitting](https://hunch.net/?p=22).





## Implementation

This section is only relevant if you have access to the model implementation. In general, this might not be the case for third-party machine learning services. Such closed models can then only be assessed based on their [output](#output) and based on the [documentation](#documentation) provided.

You can ask the following questions:

* Is the implementation correct? Does the code what it is supposed to do?
* Are the data, the model, the documentation, etc. under version control? Are you reviewing the version to be used in production?
* Has randomness been made reproducible by setting seeds? How much does this artificial noise influence the model?
* Does the model output depend on the underlying computer architecture? I encountered one example of a critical optimization algorithm that would give different results on a 32 bit and a 64 bit machine.
* Due to the fast-changing landscape of third-party machine learning services, you might want to make sure that the machine learning service you chose to develop and deploy your model will not be discontinued during the intended life-time of your model.
* If you are assessing an updated version of an older model: Have the libraries changed in the meantime?
* Only based on the documentation, can you produce a reimplementation of the model?
* Does the model’s API work correctly?
* How will the model be deployed?
* What differences will there be between the version of the model you are reviewing and the final production version? For example, will there be a reimplementation before deployment using a low-level language?
* Is model inference time relevant? 
* Are there memory constraints on your model?
* Are there any hard-coded values?
* Does the model run automatically or is human intervention required?




## Output

This section describes methods to validate a machine learning model solely based on its outputs and predictions. This section is most important if the inner workings of the model are unknown, cannot be assessed, or are simply to complex to develop an intuition for. Some methods described here require that there are no restrictions on applying the model, such as run-time or cost constraints.


### General sense-checking

Basic questions to assess whether the model makes sense. 

* Does model performance matter on average or for individual examples? It makes a difference whether the model is invoked many times and accuracy needs to be high average, or whether the model makes few predictions and for each prediction the required accuracy is very high. Consider this aspect also when assessing model stability. At the example of an automatic pricing model for an online shop, it can be very confusing if a customer sees the price of a given product vary significantly from one day to the other, although, on average over time and over all customers, the price of this product might be stable.
* Create your own test data set to estimate model performance.
* Is there bias in model results?
* Assess the materiality of the model decisions. How much does a false negative cost? Consider introducing the concept of cost-weighted accuracy.
* Discriminatory Power: Is the model able to distinguish between qualitatively different cases? This is a very basic assumption on classical models. The problem with machine learning models may be in doing this consistently for all individual cases and not only on average.
* How does the model perform on subsets of the test data? Are there any inconsistencies?.



### Benchmarking

Assess whether the model makes sense by comparing its outputs to different, possibly simpler, models.

* Perform basic sense-checking of the model output, for example by manually going through some predictions.
* Is the model better than a random prediction? For example, a model predicting a price change in the S&P500 from today to tomorrow of at most +/- 1% is not better than an uneducated guess.
* Develop your own simple benchmark model and compare its results to the full model. Are the model’s results superior enough to the simpler model’s results to justify the additional complexity?
* Compare the model to the industry standard for that application. For example, image data models could be compared to models based on ResNet-50.



### Model sensitivities

This section is about assessing how the model outputs change when some part of the model changes. There are some differences between classical models and machine learning models in how such sensitivities should be interpreted. The main example is [parameter uncertainty](#Sensitivity-of-the-model-to-parameters)


#### Sensitivity of the model to training data

The tests described here try to assess the model’s dependency on the training data. This section is only relevant in case the model can be retrained. If the model is very sensitive to the training data, this is an indication that the model will perform poorly after deployment. This might be the case if the training data is not extensive enough or if the model is not appropriate.

Retrain and test the model on the variants of the input data that reflect likely use-cases during the model’s lifecycle:

* Only use a subset of the available training data for training and see how the model performs in comparison to the full model.
* Perform cross-validation.
* The training set might change in time once the model is in production, for example in case the model will be retrained regularly after new data has been acquired. Assess stability of the model in time.
* Is the model sensitive to the removal of individual observations from the training data?
* Feature importance: Machine learning algorithms may decide to use only one feature, but you are not actually realizing it.
* Variants of data imputation, data scaling, feature engineering, etc.
* Bootstrapped variants of the training data. Fit the model to samples of the original data. Training data can be seen as a sample of a data generating process. Fitting the model to bootstrapped samples of the training data therefore tries to assess the model’s dependence on your particular random instance of training data.


#### Sensitivity of the model to varying input

Many machine learning models are highly non-linear and can even be non-continuous. This leads to increased risk of false predictions as non-linear models are not known how to behave in extreme situations outside or at the boundary of their domain.

* Does the model’s prediction reflect reality, your expectations, or the prediction by other benchmark models? Are there discontinuities of the model? For example, can a classification change between nearby input data points?
* Assess stability of model if input data deteriorates during production, for example if sensors break, cameras become foggy, measurement errors increase, etc.
* There are various machine learning model explanation techniques [based on varying input](https://christophm.github.io/interpretable-ml-book/agnostic.html).



#### Sensitivity of the model to parameters

In classical model validation, one would assess the robustness of the model under parameter uncertainty. Such sensitivity analysis to parameters is less of a criterion for a valid model when working with machine learning models. Any individual parameter and any sensitivity of the model output to an individual parameter might in fact be meaningless. For example, the performance of a neuronal network can strongly depend on the actual values of its parameters, but in a sense this does not matter, as these parameters _are_ in a sense the model.



#### Sensitivity of the model to expert judgments

Many other choices are made during model development. In classical model validation, these choices count as expert judgments and would need to be justified. In machine learning, they are seen as means to improve model performance. Model validation nevertheless needs to assess that these choices have not been made to deliberately influence the output of the model.




## Documentation

Often, machine learning model cannot be written down explicitly. Sometimes (in the case of closed third-party models), not even the type of model is known. Additionally, due to the random nature of most machine learning models, a reimplementation of the model given exactly the same results might not be possible. There are therefore special requirement on the documentation of a machine learning model as opposed to classical models.

You can ask the following questions on the model documentation:

* Is an attempt given to explain the model via illustrative examples? Are the explaining examples well chosen? 
* Have a look at techniques for [model explanation](https://christophm.github.io/book/).
* Consider using [model cards](https://arxiv.org/pdf/1810.03993.pdf) for model documentation. Model cards are an attempt to standardize machine learning model documentation and specification.
* Can a pseudo-code implementation of the model be given?
* Is the level of technicalities in the documentation appropriate for the audience?
* Is a full reimplementation possible relying only on the information provided in the documentation?
* Can you give a short high-level description of the model and its limitations?




## Governance and Use

Questions to assess whether the model can actually be used in production.

* How material is the model? How costly are mistakes of the model? 
* Do model users understand (the basics of) the model and its limitations? 
* Model misuse: Is the model only applied to the use case for which it was designed?
* Is model use outside its domain prohibited? Does the model show that it has been applied to data it has not been designed for?
* Do you comply with all relevant regulations, both within and outside of your institution?
* What requirements do regulators have on your model?

----

&copy; 2020 [Adrian Scheerer](https://www.linkedin.com/in/adrianscheerer/)
