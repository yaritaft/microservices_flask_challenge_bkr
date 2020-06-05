"""initial database migration

Revision ID: 3bfdbd4866f6
Revises: 
Create Date: 2020-06-05 15:18:03.881508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3bfdbd4866f6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "state",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["state_id"], ["state.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    op.drop_table("state")
    # ### end Alembic commands ###