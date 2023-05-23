# client.py
import asyncio
import websockets

# 서버로부터 메시지를 수신하면 출력
async def receive(websocket):
    async for message in websocket:
        print(message)

# 사용자 입력을 받아서 서버로 메시지 전송
async def send(websocket):
    while True:
        message = input("메시지 입력: ")
        await websocket.send(message)

# 서버의 IP 주소와 포트 설정
server_address = 'localhost'
server_port = 8765

# WebSocket 클라이언트 생성 및 실행
async def main():
    async with websockets.connect(f"ws://{server_address}:{server_port}") as websocket:
        tasks = [receive(websocket), send(websocket)]
        await asyncio.wait(tasks)

asyncio.get_event_loop().run_until_complete(main())
