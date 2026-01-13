from agents.intent_classifier import intent_classifier
from agents.urgency_estimator import urgency_estimator
from agents.action_router import action_router
from data.sample_emails import sample_emails

state = {
    **sample_emails[1],
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
state = action_router(state)

print("Action:", state["action"])
print("Approval required:", state["approval_required"])
print("History:", state["history"])
