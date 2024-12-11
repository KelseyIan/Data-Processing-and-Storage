# Data-Processing-and-Storage

Overview of Code:

This details data-processing storage code to effectively store transactions. Uses two Maps, one for finalized transactions and one for active transactions. This is a great way to match key value pairs, as well as key value pairs for non-committed transactions. When a transaction is finalized, the items in the temp_map are added to the finalized transaction map, and appropriate booleans are reset.

Function Overview:

  begin_transaction() -> Creates a new transaction
  
  put(key, value) -> Puts a key, value in the temporary transaction map (Handles overrides)
  
  get(key) -> Retrieves the value associated with the given key. Handles a null exception if the key is not present
  
  commit() -> Commits the changes from the transaction to the finalized transaction, handles key,value overrides if key is present or not present.
  
  Rollback () -> Reverts all the changes that were present in this current transaction.

  How to Run Code:

  1. Clone this code to your IDE or local device
  2. Ensure you have Python on your device.
  3. Ensure compatibility with your current phyton version (Update locally if needed)
  4. To test the code, create an instance of the class object then begin a transaction by calling "begin_transaction()".
  5. An example test to test the functionality is below:
     database= InMemoryDB()  
     database.begin_transaction
     database.put("A",1)
     database.commit()
     #ensure to print if the function returns a value to check output
     print(database.get("B"))  #will return error message
     print(database.get("A"))  #will return the appropriate value
6. Ensure a variety of test cases to check the robustness of the code

Future Assignment Considerations:

  I enjoyed learning and working on databases in this class and wish we worked on it more. This assignment was a great first step in seeing how to code a database in the language of your choice. I would keep the ability to choose what language to use to complete this assignment. I would modify this assessment and allow specific users to have a list of their transactions. This could be seen as a Map of Maps, with the Key being the transaction user name and value being a map of their specific transactions. Inside of this assignment, one modification to the instructions could be specific error messages that you would expect. This would keep the code more uniform between different student submissions.
  The last improvement that could help both teachers, TAs, and students is a test file or having the students create a file with unit tests. This would help the students test their code, judge their ability to create comprehensive unit tests, and help ease grading from the professor's point of view.

