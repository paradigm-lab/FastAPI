"""add content column to posts tables

Revision ID: b2d0ce3378be
Revises: c17656b1e362
Create Date: 2022-07-14 06:33:13.821986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2d0ce3378be'
down_revision = 'c17656b1e362'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
