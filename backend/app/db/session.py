from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Placeholder engine — real DB URL will come from settings later
engine = create_engine("postgresql://placeholder", echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
