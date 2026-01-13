from agents.intent_classifier import intent_classifier
from agents.urgency_estimator import urgency_estimator
from agents.action_router import action_router
from agents.reply_generator import reply_generator
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
state = action_router(state)

if state["action"].value == "reply":
    state = reply_generator(state)
    print("Draft reply:\n", state["draft_reply"])

print("History:", state["history"])
