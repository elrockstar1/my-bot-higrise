import os
import asyncio
from highrise import BaseBot, ChatEvent

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("¡El bot nuevo de Highrise está online y corriendo!")

    async def on_chat(self, user, message: str):
        # Comando de prueba en el chat de la sala
        if message.lower() == "!hola":
            await self.highrise.chat(f"¡Qué onda @{user.username}! Bienvenido.")

if __name__ == "__main__":
    from highrise.__main__ import main
    main()
