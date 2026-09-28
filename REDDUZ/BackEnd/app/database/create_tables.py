from app.database.db import engine, Base
import app.database.models  # 👈 importa TODOS os models registrados

print("Criando tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")