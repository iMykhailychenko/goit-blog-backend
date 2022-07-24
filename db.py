from databases import Database
from config import POSTGRES_PORT, POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

database = Database(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")


async def connect() -> None:
    print("Connect to Database ...")
    try:
        await database.connect()
        print('Success! Database connected')
    except BaseException as error:
        print("Error! Database is not connected")
        print(error)


async def disconnect() -> None:
    print("Disconnecting from Database ...")
    await database.disconnect()
    print("Done. Disconnected from Database")
