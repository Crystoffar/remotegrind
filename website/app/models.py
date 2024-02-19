from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Ticket(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    message: so.Mapped[str] = so.mapped_column(sa.String(512), index=True)

    def __repr__(self):
        return 'Name: {}\nEmail: {}\nMessage: \n{}'.format(self.name, self.email, self.message)