from graph.email_graph import build_email_graph
from data.sample_emails import sample_emails

graph = build_email_graph()

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

final_state = graph.invoke(state)

print("\nFINAL STATE")
for k, v in final_state.items():
    print(f"{k}: {v}")
