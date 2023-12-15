# import random
# from string import ascii_letters
# from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint
# from flask_socketio import SocketIO, join_room, leave_room, send

# # chat = Flask(__name__, '/chat')
# socketio = SocketIO(app)

# def generate_room_code(length: int, existing_codes: list[str]) -> str:
#     while True:
#         code_chars = [random.choice(ascii_letters) for _ in range(length)]
#         code = ''.join(code_chars)
#         if code not in existing_codes:
#             return code

# # @chat.route('/'):
# # def home():

# rooms = {} #комнаты(чаты)
        
# @app.route('/makeroom', methods=["GET", "POST"])
# def home():
#     session.clear()
#     if request.method == "POST":
#         name = request.form.get('name')
#         create = request.form.get('create', False)
#         code = request.form.get('code')
#         join = request.form.get('join', False)
#         if not name:
#             return render_template('user/chat1.html', error="Name is required", code=code)
#         if create != False:
#             room_code = generate_room_code(6, list(rooms.keys()))
#             new_room = {
#                 'members': 0,
#                 'messages': []
#             }
#             rooms[room_code] = new_room
#         if join != False:
#             # no code
#             if not code:
#                 return render_template('user/chat1.html', error="Please enter a room code to enter a chat room", name=name)
#             # invalid code
#             if code not in rooms:
#                 return render_template('user/chat1.html', error="Room code invalid", name=name)
#             room_code = code
#         session['room'] = room_code
#         session['name'] = name
#         return redirect(url_for('room'))
#     else:
#         return render_template('user/chat1.html')
    
# @app.route('/room')
# def room():
#     room = session.get('room')
#     name = session.get('name')
#     if name is None or room is None or room not in rooms:
#         return redirect(url_for('/'))
#     messages = rooms[room]['messages']
#     return render_template('user/room2.html', room=room, user=name, messages=messages)

# @socketio.on('connect')
# def handle_connect():
#     name = session.get('name')
#     room = session.get('room')
#     if name is None or room is None:
#         return
#     if room not in rooms:
#         leave_room(room)
#     join_room(room)
#     send({
#         "sender": "",
#         "message": f"{name} has entered the chat"
#     }, to=room)
#     rooms[room]["members"] += 1

# @socketio.on('message')
# def handle_message(payload):
#     room = session.get('room')
#     name = session.get('name')
#     if room not in rooms:
#         return
#     message = {
#         "sender": name,
#         "message": payload["message"]
#     }
#     send(message, to=room)
#     rooms[room]["messages"].append(message)

# @socketio.on('disconnect')
# def handle_disconnect():
#     room = session.get("room")
#     name = session.get("name")
#     leave_room(room)
#     if room in rooms:
#         rooms[room]["members"] -= 1
#         if rooms[room]["members"] <= 0:
#             del rooms[room]
#         send({
#         "message": f"{name} has left the chat",
#         "sender": ""
#     }, to=room)

# # if __name__ == "__main__":
# #     socketio.run(chat, debug=True)

# print("Hello world!")

# # @chat.route('/chat')
# # def chat():
# #     if 'log' in session:
# #         if session['log']:
# #             query = f"""select * from users where id={session['id']}"""
# #             cursor.execute(query)
# #             info = cursor.fetchone()
            
# #             query = f"""select * from home  where login='{info[2]}';"""
# #             cursor.execute(query)
# #             data = info[3:] + cursor.fetchone()[1:]
            
# #             col = get_col('users')[3:] + get_col('home')[1:]
        
# #             area = {col[i][0]: data[i] for i in range(len(data))}

# #             room_code = generate_room_code(6, list(rooms.keys()))
# #             room = room_code
# #             messages = rooms[room]['messages']


# #             return render_template(
# #                 'user/chat.html',
# #                 data=area,
# #                 room = room,
# #                 messages = messages
# #             )

# # @socketio.on('connect')
# # def handle_connect():
# #     name = session.get('name')
# #     room = session.get('room')
# #     if name is None or room is None:
# #         return
# #     if room not in rooms:
# #         leave_room(room)
# #     join_room(room)
# #     send({
# #         "sender": "",
# #         "message": f"{name} has entered the chat"
# #     }, to=room)
# #     rooms[room]["members"] += 1

# # @socketio.on('message')
# # def handle_message(payload):
# #     room = session.get('room')
# #     name = session.get('name')
# #     if room not in rooms:
# #         return
# #     message = {
# #         "sender": name,
# #         "message": payload["message"]
# #     }
# #     send(message, to=room)
# #     rooms[room]["messages"].append(message)

# # @socketio.on('disconnect')
# # def handle_disconnect():
# #     room = session.get("room")
# #     name = session.get("name")
# #     leave_room(room)
# #     if room in rooms:
# #         rooms[room]["members"] -= 1
# #         if rooms[room]["members"] <= 0:
# #             del rooms[room]
# #         send({
# #         "message": f"{name} has left the chat",
# #         "sender": ""
# #     }, to=room)
