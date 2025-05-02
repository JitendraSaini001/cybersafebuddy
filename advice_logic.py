def generate_advice(user_data):
    age_group = user_data.get("age", "all")
    wifi = user_data.get("wifi", "no")

    advice = []

    if age_group == "kids":
        advice.append("Never share personal info online.")
    elif age_group == "teens":
        advice.append("Be careful with strangers on the internet.")
    elif age_group == "adults":
        advice.append("Use strong passwords and enable 2FA.")
    elif age_group == "50plus":
        advice.append("Be cautious of phishing emails and scams.")
    else:
        advice.append("Practice safe browsing habits.")

    if wifi == "yes":
        advice.append("Use a secure password on your WiFi.")
    else:
        advice.append("Avoid using open/public WiFi networks.")

    return advice
