from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    # Extracting 'uid' parameter from the query string
    uid = request.args.get('uid')
    if not uid:
        return "Error: UID not provided", 400, {'Content-Type': 'text/plain; charset=utf-8'}
    
    url = f"https://freefire-virusteam.vercel.app/glfflike?uid={uid}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "status" in data and data["status"] == "Success":
            # Extracting Guild-related information
            guild_info = data.get("Guild Information", {})
            
            guild_name = guild_info.get("Guild Name", "Not available")
            guild_id = guild_info.get("Guild ID", "Not available")
            guild_level = guild_info.get("Guild Level", "Not available")
            guild_capacity = guild_info.get("Guild Capacity", "Not available")
            guild_current_members = guild_info.get("Guild Current Members", "Not available")
            leader_ac_create_time = guild_info.get("Leader Ac Created Time", "Not available")
            
            return f"""GUILD NAME : {guild_name}
GUILD ID : {guild_id}
GUILD LEVEL : {guild_level}
GUILD CAPACITY : {guild_capacity}
GUILD CURRENT MEMBERS : {guild_current_members}

LEADER AC CREATE TIME : {leader_ac_create_time}""", 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
        else:
            return "Error: Status is not Success or Guild Information not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
