from enum import Enum


class ErrorMessage(str, Enum):
    SignatureIssue = "The signature was incorrect"
    TypeIssue = "Encountered an issue converting the public key"
    ValueIssue = "This likely means the public key is incorrect or not set"
