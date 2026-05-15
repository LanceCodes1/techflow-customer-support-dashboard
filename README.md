# Phase 1: Weeks 9 + 10 - Project Instructions
Using the [Guided Exercise: Python, SQLAlchemy, SQLite, and Streamlit](https://github.com/AI-for-Business-Solutions/p1w5_jupyter_materials/blob/main/hw_p1w5_guided_exercise.ipynb) as a beacon (not hard set instructions), the fellow will be provided with a set of case studies that they have to develop a technical solution for, similar to the week 5 project.

**Fellows will pick *one (1) of the three (3)* case studies to develop a solution for, based on research they've conducted for various `faker` generators.**

While context for the case study will be provided, the code necessary to develop the solution will not. The fellows will be graded based on their ability to address the business problem presented in the case study and in developing the technical solution from start to finish.

Fellows should expect that they will provide the technical implementation for generating the data that best represents what is being provided in the case study, as well as the means to visualize the data using `SQLAlchemy`. Their data should effectively export using `pandas` to generate a `.csv` file to later be used with Lovable to create a dashboard with their sample findings.

**Refer to your chosen case study's markdown file to follow the explicit instructions per each study.**

## Week 9
Follow a similar cadence as the original Phase 1: Week 5 - Python + SQL Graded Project:
1. Set up your project
    1. Ensure you are able to effectively connect the SQL database using SQLTools
3. Create a virtual environment for your Python project
    1. Ensure you are able to activate and deactivate the virtual environment through the terminal
    2. Export your packages to a `requirements.txt` file
4. Create a database connect to your `database.py` file
5. Define your models based on the case study
    1. Check the `Required Data` section of the case study that determines the data required in your models and tables
    2. Use Faker generators to emulate data that most closely relate to the data type of each key in your models
        1. For example, each case study requires at least one `UUID`, so we would consult Faker to find a generator that would create a random `UUID`, and we would find [uuid4 in the `misc` section of Faker's generator](https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html)
7. Set up your helper functions
8. Create a seed file in your project
    1. Ensure you are importing your packages, including Faker
    2. Using the `How to Use Data` section, create code that will emulate the desired behavior

## Week 10
Continue following a similar cadence as the original Phase 1: Week 5 - Python + SQL Graded Project:
1. Set up an `app.py` file to create a `session` for your database, and to load the data generated with your individual case study's functions
    1. Example: The Week 5 project defined a function that would computer a product information score using `compute_information_score_for_product` based off the original `compute_information_score` inside the `seed.py` file to allow `SQLalchemy` to determine what data to display in our tables
    2. Model your `app.py` based on the same desired outcome
    3. **DO NOT** create the sidebar form, as we're not creating new data, only *loading* the data (refer to the `load` functions we previously used)
    4. Test that when running `SQLalchemy`, you can effectively generate the tables per your respective case study.
2. Create an `export.py` file that will export the `.csv` files we'll need for Lovable
    1. At the end of each ` How to Use the Data` section of your chose case study, the table that generates a dataframe with `pandas` will be the same table we want to export for our `.csv` file
3. Once the `.csv` file is exported, use the `Sample Findings from Generated Data` section to engineer a prompt you will provide Lovable in order to create a dashboard of your sample findings with your given set of data
4. Create a brief [business memo](https://www.bing.com/search?pglt=299&q=business+memos&cvid=5815c46e16f5479f99c1687a5d5185ef&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgyMDcyajBqMagCALACAA&FORM=ANNTA1&adppc=EDGEESS&PC=SMTS) with the recommended solution to the business issue
5. A short presentation of the sample findings from your dataset to your hypothetic "management"