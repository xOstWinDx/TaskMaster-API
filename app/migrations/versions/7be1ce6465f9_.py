"""empty message

Revision ID: 7be1ce6465f9
Revises: e3ed6e80c39a
Create Date: 2024-04-22 01:03:36.151133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7be1ce6465f9'
down_revision: Union[str, None] = 'e3ed6e80c39a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('status', sa.Boolean(), server_default='False', nullable=False))
    op.drop_column('task', 'expired')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('expired', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.drop_column('task', 'status')
    # ### end Alembic commands ###
