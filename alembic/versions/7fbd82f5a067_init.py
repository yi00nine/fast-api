"""init

Revision ID: 7fbd82f5a067
Revises: 
Create Date: 2023-12-23 16:34:24.978621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fbd82f5a067'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False, comment='datasetID'),
    sa.Column('name', sa.String(length=50), nullable=False, comment='名称'),
    sa.Column('major', sa.String(length=50), nullable=False, comment='专业'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_major'), 'test', ['major'], unique=False)
    op.create_index(op.f('ix_test_name'), 'test', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_name'), table_name='test')
    op.drop_index(op.f('ix_test_major'), table_name='test')
    op.drop_table('test')
    # ### end Alembic commands ###
