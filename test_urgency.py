from agents.intent_classifier import intent_classifier
from agents.urgency_estimator import urgency_estimator
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

state = intent_classifier(state)
state = urgency_estimator(state)

print(state["urgency"])
print(state["sla_deadline"])
print(state["history"])
