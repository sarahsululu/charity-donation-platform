from .db_connection import get_db_connection
from .data_models import Campaign, Donation

def create_campaign(title, description, goal_amount):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO campaigns (title, description, goal_amount) VALUES (?, ?, ?)",
              (title, description, goal_amount))
    conn.commit()
    conn.close()
    print("Campaign created!")

def list_campaigns():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM campaigns")
    rows = c.fetchall()
    conn.close()
    campaigns = [Campaign(r["id"], r["title"], r["description"], r["goal_amount"], r["current_amount"]) for r in rows]
    return campaigns

def make_donation(user_id, campaign_id, amount, message=None):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO donations (user_id, campaign_id, amount, message) VALUES (?, ?, ?, ?)",
              (user_id, campaign_id, amount, message))
    c.execute("UPDATE campaigns SET current_amount = current_amount + ? WHERE id = ?", (amount, campaign_id))
    conn.commit()
    conn.close()
    print("Donation successful!")
