def analyze_password(password,
                     min_length=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):
    is_strong = True
    count_active_rules = 0
    count_rules = 0
    missing_rules = []
    if min_length > 0:
        count_active_rules += 1
    if len(password) < min_length:
        is_strong = False
        missing_rules.append("min_length")
    else:
        count_rules += 1
    if require_digit:
        count_active_rules +=1
    score_percent = count_active_rules / count_rules * 100
    return is_strong, score_percent, missing_rules

print(analyze_password("abcdefgh", 5,False,
                       True,True, [123]))
print(analyze_password("12345678",require_symbol=False))
