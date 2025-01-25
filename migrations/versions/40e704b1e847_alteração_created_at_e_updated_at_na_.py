"""alteração created_at e updated_at na tabela todos

Revision ID: 40e704b1e847
Revises: 97887a7fcce0
Create Date: 2025-01-25 11:06:26.407389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40e704b1e847'
down_revision: Union[str, None] = '97887a7fcce0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.drop_column('todos', 'update_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('update_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.drop_column('todos', 'updated_at')
    # ### end Alembic commands ###
