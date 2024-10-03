
def top_note(data):
	return {"name": data["name"], "top_note": max(data["notes"])}

print(top_note({"name": "John", "notes":[12,20,17,19,18]}))