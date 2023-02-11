def check_score_greater(movie): 
    if(movie['imdb']>5.5):
        return True
    else:
        return False

print ('')
print ('Checking if Dark Knight is greater than 5.5')
print ('')
is_greater=check_score_greater(movie[2])
if(is_greater):
    print ('True')
else :
    print ('False')