from langchain_ollama import ChatOllama
llm = ChatOllama(model="gemma3:4b")
subject = input("Email subject: ")
email = input("Paste an email to classify: ")
if not subject.strip() or not email.strip():
    print("Please enter both a subject and email text.")
    raise SystemExit
prompt= f"Classify this email as work, personal, or spam. Reply with only one category.\n\n subject: {subject} Email: {email}"
try:
    response = llm.invoke(prompt)
except Exception as error:
    print("Could not reach Ollama. Make sure it is running.")
    raise SystemExit(1) from error
print (response.content)
category = response.content.strip().lower()
if category not in {"work", "personal", "spam"}:
    print("The model returned an unexpected category. Please review this email manually.")
    exit()
print("Valid category:", category in {"work", "personal", "spam"})
if category == "work":
    print("Action: move to Work")
elif category == "personal":
    print("Action: move to Personal")
elif category == "spam":
    print("Action: review as spam")
else:
    print("Action: review manually")

