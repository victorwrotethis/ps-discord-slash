from enum import Enum


class ErrorMessage(str, Enum):
    SignatureIssue = "The signature was incorrect"
    TypeIssue = "Encountered an issue converting the public key"
    ValueIssue = "This likely means the public key is incorrect or not set"

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self
