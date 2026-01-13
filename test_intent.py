from agents.intent_classifier import intent_classifier
from data.sample_emails import sample_emails

state = {
    **sample_emails[0],
    "intent": None,
    "urgency": None,
    "action": None,
    "draft_reply": None,
    "approval_required": None,
    "approved": None,
    "follow_up_date": None,
    "sla_deadline": None,
    "sla_violated": None,
    "history": []
}

updated_state = intent_classifier(state)
print(updated_state["intent"])
print(updated_state["history"])
