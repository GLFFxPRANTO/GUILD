from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_ff_info(uid):
    url = f"https://freefire-info.fly.dev/{uid}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extracting Basic Info
        basic = data.get("basicinfo", [{}])[0]
        username = basic.get("username", "N/A")
        level = basic.get("level", "N/A")
        likes = basic.get("likes", "N/A")
        region = basic.get("region", "N/A")
        last_login = basic.get("lastlogin", "N/A")
        bio = basic.get("bio", "N/A")
        exp = basic.get("Exp", "N/A")
        ob = basic.get("OB", "N/A")
        avatar = basic.get("avatar", "N/A")
        banner = basic.get("banner", "N/A")

        # Extracting Clan Admin Info
        clan_admin = data.get("clanadmin", [{}])[0]
        admin_name = clan_admin.get("adminname", "N/A")
        br_point = clan_admin.get("brpoint", "N/A")
        cs_point = clan_admin.get("cspoint", "N/A")
        admin_exp = clan_admin.get("exp", "N/A")
        id_admin = clan_admin.get("idadmin", "N/A")

        # Extracting Clan Info
        clan_info = data.get("claninfo", [{}])[0]
        clan_id = clan_info.get("clanid", "N/A")
        clan_name = clan_info.get("clanname", "N/A")
        guild_level = clan_info.get("guildlevel", "N/A")
        live_member = clan_info.get("livemember", "N/A")

        # JSON Response
        result = {
            "Username": username,
            "Level": level,
            "Likes": likes,
            "Region": region,
            "Last Login": last_login,
            "Bio": bio,
            "Exp": exp,
            "OB": ob,
            "Avatar": avatar,
            "Banner": banner,
            "ClanAdmin": {
                "Admin Name": admin_name,
                "BR Point": br_point,
                "CS Point": cs_point,
                "Exp": admin_exp,
                "ID Admin": id_admin
            },
            "ClanInfo": {
                "Clan ID": clan_id,
                "Clan Name": clan_name,
                "Guild Level": guild_level,
                "Live Members": live_member
            }
        }
        return result
    else:
        return {"error": f"Failed to fetch data. Status Code: {response.status_code}"}

@app.route('/freefire/<uid>', methods=['GET'])
def get_freefire_info(uid):
    return jsonify(fetch_ff_info(uid))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
