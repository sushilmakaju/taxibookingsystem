import re


def mobvalidation(mobile):
    regg=re.compile("^(?:0|\+?977)\s?(?:\d\s?){9,11}$")
    if re.fullmatch(regg, mobile):
        Result=True
    else:
        Result=False

    return Result

def passvalidation(password):
    #Minimum eight characters, at least one uppercase letter,
    # one lowercase letter, one number and one special character
    regex=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if re.fullmatch(regex, password):
        passwordResult=True
    else:
        passwordResult=False
    return passwordResult

def usernamevalidation(username):
    regex=re.compile("^([a-z]{1,6}[ ']){0,3}([ÉÈÊËÜÛÎÔÄÏÖÄÅÇA-Z]{1}[éèëêüûçîôâïöäåa-z]{2,}[- ']){0,3}[A-Z]{1}[éèëêüûçîôâïöäåa-z]{2,}$")
    if re.fullmatch(regex,username):
        usernameresult = True
    else:
        usernameresult = False
    return usernameresult

def namevalidation(name):
    regex=re.compile("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    if re.fullmatch(regex, name):
        nameResult=True
    else:
        nameResult=False
    return nameResult
