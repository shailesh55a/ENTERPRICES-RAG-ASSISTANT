def initialize_chat():

    return []

def add_message(history, role, content):

    history.append({
        "role": role,
        "content": content
    })

    return history