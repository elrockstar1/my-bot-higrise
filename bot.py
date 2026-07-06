import os
import asyncio
from highrise import BaseBot, ChatEvent
from highrise.__main__ import main

class MiBotHighrise(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("¡El bot de Highrise está online y corriendo en Railway!")

    async def on_chat(self, user, message: str) -> None:
        # Comando de prueba en el chat de la sala
        if message.lower() == "!hola":
            await self.highrise.chat(f"¡Qué onda @{user.username}! Bienvenido a la sala.")

if __name__ == "__main__":
    # Esto lee automáticamente el Token de Railway. 
    # Pon aquí abajo el ID de tu sala de Highrise reemplazando los ceros:
    room_id = os.environ.get("ROOM_ID", "000000000000000000000000")
    api_token = os.environ.get("API_TOKEN")
    
    if not api_token:
        print("Error: No se encontró el API_TOKEN en las variables de entorno.")
    else:
        asyncio.run(main(f"bot:MiBotHighrise", room_id, api_token))
