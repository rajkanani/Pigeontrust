import random
import os
import flask
from flask import request
from validate_email import validate_email
import string

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test', methods=['GET'])
def test():
    return "<h1>Welcome Back Again</h1><p>This is email verifier tool v1.</p>"

@app.route('/email_check', methods=['GET'])
def email_checker():
    try:
        email = request.args.get('email')
        is_valid = validate_email(email_address=email,
                                  check_format=True,
                                  check_blacklist=True,
                                  check_dns=True,
                                  dns_timeout=10,
                                  check_smtp=True,
                                  smtp_timeout=10,
                                  smtp_helo_host='my.host.name',
                                  smtp_from_address='my@from.addr.ess',
                                  smtp_debug=False)
        return {'is_success': is_valid}
    except Exception as e:
        print("Error:", e)
        return {'is_success': False}

@app.route('/cross_verify', methods=['GET'])
def hard_verify():
    try:
        email = request.args.get('email')
        is_valid_original = validate_email(email_address=email,
                                            check_format=True,
                                            check_blacklist=True,
                                            check_dns=True,
                                            dns_timeout=10,
                                            check_smtp=True,
                                            smtp_timeout=10,
                                            smtp_helo_host='my.host.name',
                                            smtp_from_address='my@from.addr.ess',
                                            smtp_debug=False)
        if is_valid_original:
            random_email = generate_random_email(email)
            is_valid_dummy = validate_email(email_address=random_email,
                                             check_format=True,
                                             check_blacklist=True,
                                             check_dns=True,
                                             dns_timeout=10,
                                             check_smtp=True,
                                             smtp_timeout=10,
                                             smtp_helo_host='my.host.name',
                                             smtp_from_address='my@from.addr.ess',
                                             smtp_debug=False)
            return {'is_success': not is_valid_dummy}
        else:
            return {'is_success': False}
    except Exception as e:
        print("Error:", e)
        return {'is_success': False}

def generate_random_email(email):
    random_part = generate_random_string(10)
    domain = email.split("@")[-1]
    return f"{random_part}@{domain}"

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
