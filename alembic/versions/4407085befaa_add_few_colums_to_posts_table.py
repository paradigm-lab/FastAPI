"""add few colums to posts table

Revision ID: 4407085befaa
Revises: b1f9c246613b
Create Date: 2022-07-14 06:59:47.977892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4407085befaa'
down_revision = 'b1f9c246613b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()"))
                  )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
