# WattWise
A Kiosk which facilitates test generation and checking.

## Naming Convention
Naming convention in programming refers to a set of rules and guidelines used to name variables, functions, classes, and other programmatic elements in a consistent and meaningful way. Having a well-defined naming convention is essential for writing readable, maintainable, and understandable code. It helps developers to quickly identify the purpose and scope of a variable or function just by looking at its name. This is especially important when working with large codebases or collaborating with other developers. 

Here are the recommended naming conventions which will be followed in developing WattWise:  

- For __views__, *\<name\>_view.py*.

   ```
   user_model.py
   ```
- For __models__, *\<name\>_model.py*. 

   ```
   login_view.py
   ```

## Models
Model is responsible for managing data and the rules that govern its behavior. It contains the application's core logic and handles tasks such as validation, data storage, and retrieval. In short, the models are responsible for managing data inside the database and the business logic of WattWise.

1. user_model
    * Model for Accounts database processes, especially for logging in and creating accounts

2. admin_model
    * Model for Admin database processes

3. board_examiner_model 
    * Model for Board Examiner database processes

## Views
The view is completely separate from the model. It does not contain any application logic, but simply presents the data managed by the model to the user. The view receives data from the model, formats it for display. Basically, the views are responsible for presenting data to the user.

1. create_account_view
    * View for creating accounts

2. login_view
    * View for user logging in 
