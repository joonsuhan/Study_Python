# server.py
import asyncio
import websockets

# 클라이언트들의 WebSocket 연결을 관리하는 서버
async def server(websocket, path):
    # 새로운 클라이언트 연결 시, 클라이언트 목록에 추가
    clients.add(websocket)
    try:
        async for message in websocket:
            # 메시지를 받으면 다른 클라이언트들에게 브로드캐스트
            await broadcast(message)
    finally:
        # 클라이언트 연결 종료 시, 클라이언트 목록에서 제거
        clients.remove(websocket)

# 모든 클라이언트들에게 메시지를 브로드캐스트
async def broadcast(message):
    for client in clients:
        await client.send(message)

# 서버의 IP 주소와 포트 설정
server_address = 'localhost'
server_port = 8765

# 클라이언트들의 WebSocket 연결을 저장하는 집합
clients = set()

# WebSocket 서버 생성 및 실행
start_server = websockets.serve(server, server_address, server_port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
