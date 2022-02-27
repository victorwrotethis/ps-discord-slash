

class TokenRequestInfo:

    def __init__(self, requester_id: int, approved_ids: [int], group_name: str):
        self.requester_id = requester_id
        self.approved_ids = approved_ids
        self.group_name = group_name
