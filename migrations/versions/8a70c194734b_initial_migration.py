"""Initial migration.

Revision ID: 8a70c194734b
Revises:
Create Date: 2023-02-21 22:07:50.407733

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '8a70c194734b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE categories_table SET SCHEMA {SCHEMA};")

    op.create_table('games_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('developer', sa.String(length=255), nullable=False),
    sa.Column('publisher', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('featured_banner_url', sa.String(), nullable=True),
    sa.Column('main_banner_url', sa.String(length=1000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE games_Table SET SCHEMA {SCHEMA};")

    op.create_table('users_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=120), nullable=False),
    sa.Column('display_pic', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users_table SET SCHEMA {SCHEMA};")

    op.create_table('cart_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE cart_table SET SCHEMA {SCHEMA};")

    op.create_table('game_categories_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories_table.id'], ),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE game_categories_table SET SCHEMA {SCHEMA};")

    op.create_table('game_screenshots_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('screenshot_url', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE game_screenshots_table SET SCHEMA {SCHEMA};")

    op.create_table('libraries_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE libraries_table SET SCHEMA {SCHEMA};")

    op.create_table('reviews_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('recommended', sa.Boolean(), nullable=False),
    sa.Column('review', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users_table.id'], ),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE reviews_table SET SCHEMA {SCHEMA};")

    op.create_table('wishlist_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games_table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE wishlist_table SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlist_table')
    op.drop_table('reviews_table')
    op.drop_table('libraries_table')
    op.drop_table('game_screenshots_table')
    op.drop_table('game_categories_table')
    op.drop_table('cart_table')
    op.drop_table('users_table')
    op.drop_table('games_table')
    op.drop_table('categories_table')
    # ### end Alembic commands ###
