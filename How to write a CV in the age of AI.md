# How to write a CV in the age of AI

Tools used in this example:
* Claude.ai (access to Projects, cost: 20 USD per month)
* Optional: Install https://wkhtmltopdf.org/ and https://pandoc.org/ 

I followed the following steps:
* Ask the LLM:
  * To create a list of necessary and optional sections in CV
  * What are best practice writing guidelines for CVs
  * To create a professional html template for a CV with CSS formatting suitable for printing
* Add these information to a new Claude project as files
* Upload your own CV, the job ad, and an extract of your LinkedIn profile, and any other information you think might be helpful
* Ask the LLM to fill in the template CV based on the information provided
* Convert the html to PDF:
  * Either by opening the html file in a browser and saving it to PDF,
  * or with the following command: wkhtmltopdf --enable-local-file-access CV.html CV.pdf
* Alternatively you could convert the html to word with the command pandoc CV.html -o CV.docx and further edit it there
* Similar steps should work with a letter of motivation

Observations:
* This is a basic automation workflow and took me less than an hour to set up. The time to get a first working prototype is much reduced compared to the classical way of fully manually writing a CV and tailoring your application to the position.
* It still takes time to make a proper professional solution, for example if you have errors in the formatting of the automatically generated files. Currently I don't know whether AI also reduces the time to a full professional solution as much as it reduces the time to a first working prototype.
* You absolutely need to review the AI output.

Personally, I don't actually recommend following an approach like this and would definitely recommend to still write everything by yourself. The background to this post is that I worked on a project to automate this process and found the above workflow which is essentially trivial and achieves what I wanted. Now I can work on other projects!

I sometimes review CVs, please don't hesitate to reach out. I got [positive feedback](https://github.com/adrische/quant-jobs-zurich/blob/master/CV-review-feedback.txt).
