from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

#Temporary Database for places
class Place(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    address: so.Mapped[str] = so.mapped_column(sa.String(64))
    latitude: so.Mapped[float] = so.mapped_column(sa.Float())
    longitude:so.Mapped[float] = so.mapped_column(sa.Float())

    def __repr__(self):
        return '<Name {}>'.format(self.name)