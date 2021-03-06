from datetime import datetime

from mosp.bootstrap import db


class Organization(db.Model):
    """Represent an organization."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500), default="")
    organization_type = db.Column(db.String(100), default="")
    website = db.Column(db.String(100), default="")
    last_updated = db.Column(db.DateTime(), default=datetime.utcnow)

    is_membership_restricted = db.Column(db.Boolean(), default=True)

    # relationship
    objects = db.relationship(
        "JsonObject",
        backref="organization",
        lazy="dynamic",
        cascade="all,delete-orphan",
    )
    schemas = db.relationship(
        "Schema", backref="organization", lazy="dynamic", cascade="all,delete-orphan"
    )

    def __str__(self):
        return self.name

    def __eq__(self, obj):
        return self.id == obj.id
