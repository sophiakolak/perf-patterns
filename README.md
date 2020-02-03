# README

## diff.py 

For each user, computes number of attempts to pass the challenge, whether or not each attempt was successful, the score change between attempts, the language used, and the diff between attempts displayed in html. 

To view the html in your browser, follow these steps: 

1. Configure the database 
2. Change the appropriate variables in mysql.connector
    ```
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=<your_password>, 
        database=<your_db_name>
    )
    ```
3. run 
    `diff.py > diff.html` 
4. Start a local server by running 
    `python3 -m http.server 1234` 
5. In your browser, go to <http://localhost:1234/diff.html> to see the diffs and other data      
