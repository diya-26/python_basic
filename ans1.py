def is_valid_ip(ip):
    try:
        parts=ip.split(".")

        if(len(parts)!=4):
            return "Invalid Ip"
        for part in parts:
            if not part.isdigit():
                return "invalid"
            num =int(part)
            if num <0 or num >255:
                return "invalid"
        return "valid ip"
    except Exception as e:
        return f"Error: {str(e)}"

def is_valid_mail(mail):
    try:
        if "@gmail.com" not in mail:
            return "not a valid mail id"
        username , domain =mail.split('@')
        if domain.lower()!="gmail.com":
            return "invalid"
        a={'.','_'}
        for char in username:
            if not(char.islower() or char.isdigit() or char in a):
                return "invalid"
        return "valid"
    except Exception as e:
        return f"Error: {str(e)}"

ip_inpt=input("Enter ip address")
email=input("Enter mail:")
print(f"{ip_inpt}:{is_valid_ip(ip_inpt)}")
print(f"{email}:{is_valid_mail(email)}")