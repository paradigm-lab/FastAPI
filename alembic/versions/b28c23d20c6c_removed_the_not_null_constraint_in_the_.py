"""Removed the NOT NULL constraint in the users table column phone number

Revision ID: b28c23d20c6c
Revises: 64ce7cc9b99b
Create Date: 2022-07-15 12:43:07.771522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b28c23d20c6c'
down_revision = '64ce7cc9b99b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
