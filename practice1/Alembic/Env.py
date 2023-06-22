from Create_table3 import Base
from alembic import context
from sqlalchemy import create_engine
from logging.config import fileConfig

target_metadata = Base.metadata


def run_migrations_offline():
    url='postgresql://postgres:postgres@localhost:5432/postgres'

    context.configer
def run_migrations_online():
    engine = engine_from_config(
                config.get_section(config.config_ini_section), prefix='sqlalchemy.')

    with engine.connect() as connection:
        context.configure(
                    connection=connection,
                    target_metadata=target_metadata
                    )

        with context.begin_transaction():
            context.run_migrations()
