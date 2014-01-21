"""create todo item table

Revision ID: 1c70a50d7e5d
Revises: None
Create Date: 2014-01-21 01:08:53.057607

"""

# revision identifiers, used by Alembic.
revision = '1c70a50d7e5d'
down_revision = None

from os import path
from alembic import op
import sqlalchemy as sa
from hello.models import db



def upgrade():
    db.create_all()
    # then, load the Alembic configuration and generate the
    # version table, "stamping" it with the most recent rev:
    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config(path.join(path.dirname(path.abspath(__file__)),
                                   "../../alembic.ini"))
    command.stamp(alembic_cfg, "head")

    pass


def downgrade():
    pass
