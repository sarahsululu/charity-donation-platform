
class User:
    def __init__(self, id, username, email, password, full_name):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name

class Campaign:
    def __init__(self, id, title, description, goal_amount, current_amount):
        self.id = id
        self.title = title
        self.description = description
        self.goal_amount = goal_amount
        self.current_amount = current_amount

class Donation:
    def __init__(self, id, user_id, campaign_id, amount, message):
        self.id = id
        self.user_id = user_id
        self.campaign_id = campaign_id
        self.amount = amount
        self.message = message
