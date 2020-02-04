import mysql.connector 

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="sDK654076$$", 
        database="hacker"
)

mycursor = mydb.cursor(buffered=True)

def get_challenge_hash():
    command = 'SELECT DISTINCT encrypted_challenge_id_hash FROM temp_dump'
    mycursor.execute(command)
    result = mycursor.fetchall()
    return result

def get_average(hash):
    command = 'SELECT AVG(totalscore) FROM temp_dump WHERE encrypted_challenge_id_hash="'+hash+'"'
    mycursor.execute(command)
    result = mycursor.fetchone()
    return result

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


def main():
    hashes = get_challenge_hash()
    print("av_score,av_num_subs")
    for hash in hashes:
        avg = get_average(hash[0])
        num = get_num(hash[0])
        u_num = get_num_unique(hash[0])
        avg_subs = num[0] / u_num[0]
        print(str(avg[0])+","+str(avg_subs))
        #print("hash:", hash[0]+", avrg score:", str(avg[0])+", total subs:", str(num[0])+", unique users:", str(u_num[0])+", avrg subs per user:", avg_subs )



if __name__=='__main__': main()
