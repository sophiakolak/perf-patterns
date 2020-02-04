import mysql.connector 
import difflib
from tabulate import tabulate
import sys
import os.path
from os import path
import os 
from collections import defaultdict 
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ['your_env_variable'], 
        database="hacker"
)

mycursor = mydb.cursor(buffered=True)

def get_challenge_hash():
    command = 'SELECT DISTINCT encrypted_challenge_id_hash FROM temp_dump'
    mycursor.execute(command)
    result = mycursor.fetchall()
    return result

def print_terminal(old, new, old_score, new_score):
    dif2 = difflib.unified_diff(StringIO(old).readlines(),
                            StringIO(new).readlines(),
                            fromfile="old version, score: "+old_score,
                            tofile="new version, score: "+new_score,
                            n=0,
                            lineterm="")
    dif_wr(dif2)

def dif_wr(d):
    for i, line in enumerate(d):
        sys.stdout.write('{} {}\n'.format(i + 1, line.strip()))

def get_num(hash):
    command = 'SELECT COUNT(*) FROM temp_dump WHERE encrypted_challenge_id_hash="'+hash+'"'
    mycursor.execute(command)
    result = mycursor.fetchone()
    return result

def get_num_unique(hash):
    command = 'SELECT COUNT(DISTINCT encrypted_user_hash) FROM temp_dump WHERE encrypted_challenge_id_hash="'+hash+'"'
    mycursor.execute(command)
    result = mycursor.fetchone()
    return result

def get_user(challenge_hash):
    command = 'SELECT DISTINCT(encrypted_user_hash) FROM temp_dump WHERE encrypted_challenge_id_hash="'+challenge_hash+'"'
    mycursor.execute(command)
    result = mycursor.fetchall()
    return result

def get_user_code(user_hash):
    command = 'SELECT code, totalscore, lang, solved FROM temp_dump WHERE encrypted_user_hash="'+user_hash+'"'
    mycursor.execute(command)
    result = mycursor.fetchall()
    return result

def main():
    #hashes = get_challenge_hash()
    easy ="3eb7480db63220b657fb9e03350c436a"
    hard = "61f4c9c54db80350ab53cdab8935f4f5"
    users = get_user(easy) 
    for user in users:
        print("<p> USER: ", user[0])
        code_versions = get_user_code(user[0])
        print("# of ATTEMPTS: ", len(code_versions),"</p>")
        for i in range(len(code_versions)):
            if i == 0:
                continue
            else: 
                old = code_versions[i-1][0]
                new = code_versions[i][0]
                old_score = str(code_versions[i-1][1])
                new_score = str(code_versions[i][1])
                old_lang = code_versions[i-1][2] 
                new_lang = code_versions[i][2]
                solved_before = str(code_versions[i-1][3])
                solved_after = str(code_versions[i][3])
                table = [['old_score', old_score],['new_score', new_score],['old_lang', old_lang],['new_lang', new_lang],['solved_before', solved_before],['solved_after', solved_after]]
                print(tabulate(table, tablefmt='html'))
                a = difflib.HtmlDiff(wrapcolumn=90)
                b = a.make_file(StringIO(old).readlines(), StringIO(new).readlines()) 
                print(b)
        print("<p> END USER", user[0], "\n </p>")
        


if __name__=='__main__': main()
