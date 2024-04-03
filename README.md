# Pigeontrust

Pigeontrust is an open-source Python library designed to verify the trustworthiness and availability of email addresses. It provides functionalities to determine whether an email address is valid, actively used, and trustworthy, aiding in email verification and validation processes within applications.

## Features

- **Email Verification**: Verify the validity of email addresses through various checks.
- **Trustworthiness Check**: Determine the trust level associated with an email address.
- **Availability Check**: Assess whether an email address is actively used and responsive.
- **Simple Integration**: Easy-to-use Python API for seamless integration into your projects.

## Installation

You can install Pigeontrust via pip:

```bash
pip install pigeontrust
```

## Usage
```python
from pigeontrust import Pigeontrust

# Initialize Pigeontrust
pigeon = Pigeontrust()

# Verify an email address
email = "example@email.com"
verification_result = pigeon.verify(email)

# Get trustworthiness score
trust_score = pigeon.trustworthiness(email)

# Check availability
availability = pigeon.check_availability(email)
```

## Contributing
Contributions are welcome! If you'd like to contribute to Pigeontrust, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your_branch_name).
3. Make your changes.
4. Commit your changes (git commit -am 'Add some feature').
5. Push to the branch (git push origin feature/your_branch_name).
6. Create a new Pull Request.

Please make sure to update tests as appropriate.

## License
Pigeontrust is licensed under the MIT License.
