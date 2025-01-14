from dataclasses import dataclass
from typing import List, Optional

import typer

from neosctl import util
from neosctl.services.gateway import schema


@dataclass
class EntityArgGenerator:
    """Argument generator for entities."""

    entity_name: str

    @property
    def identifier(self):  # noqa: ANN201
        """Argument identifier."""
        return typer.Argument(..., help=f"{self.entity_name} identifier", callback=util.sanitize)

    @property
    def name(self):  # noqa: ANN201
        """Argument name."""
        return typer.Argument(..., help=f"{self.entity_name} name", callback=util.sanitize)

    @property
    def label(self):  # noqa: ANN201
        """Argument label."""
        return typer.Argument(..., help=f"{self.entity_name} label", callback=util.sanitize)

    @property
    def description(self):  # noqa: ANN201
        """Argument description."""
        return typer.Argument(..., help=f"{self.entity_name} description", callback=util.sanitize)

    @property
    def note(self):  # noqa: ANN201
        """Argument note."""
        return typer.Argument(..., help=f"{self.entity_name} note", callback=util.sanitize)

    @property
    def owner(self):  # noqa: ANN201
        """Argument owner."""
        return typer.Option(..., "--owner", "-o", help=f"{self.entity_name} owner", callback=util.sanitize)

    @property
    def owner_optional(self):  # noqa: ANN201
        """Argument optional owner."""
        return typer.Option(None, "--owner", "-o", help=f"{self.entity_name} owner", callback=util.sanitize)

    @property
    def contacts(self):  # noqa: ANN201
        """Argument contacts."""
        return typer.Option([], "--contact", "-c", help=f"{self.entity_name} contact IDs", callback=util.sanitize)

    @property
    def links(self):  # noqa: ANN201
        """Argument links."""
        return typer.Option([], "--link", "-l", help=f"{self.entity_name} links", callback=util.sanitize)


def create_entity(
    ctx: typer.Context,
    url_prefix: str,
    label: str,
    name: str,
    description: str,
    owner: Optional[str],
    contacts: List[str],
    links: List[str],
    entity_schema: Optional[schema.CreateEntity] = None,
) -> None:
    """Create entity."""
    if owner is None:
        if len(contacts) == 0 and len(links) == 0:
            info = None
        else:
            raise util.exit_with_output(
                msg="Set info fields: owner (required), constacts (optional) and links (optional).",
                exit_code=1,
            )
    else:
        info = schema.EntityInfo(
            owner=owner,
            contact_ids=contacts,
            links=links,
        )

    if entity_schema is None:
        entity_schema = schema.CreateEntity(
            name=name,
            label=label,
            description=description,
        )

    data = schema.CreateEntityRequest(
        entity=entity_schema,
        entity_info=info,
    )

    util.post_and_process(
        ctx,
        url_prefix,
        json=data.dict(exclude_none=True, by_alias=True),
    )


def list_entities(ctx: typer.Context, url_prefix: str) -> None:
    """List entities."""
    util.get_and_process(ctx, url_prefix)


def get_entity(ctx: typer.Context, url_prefix: str, identifier: str) -> None:
    """Get entity."""
    util.get_and_process(ctx, f"{url_prefix}/{identifier}")


def delete_entity(ctx: typer.Context, url_prefix: str, identifier: str) -> None:
    """Delete entity."""
    util.delete_and_process(ctx, f"{url_prefix}/{identifier}")


def update_entity(
    ctx: typer.Context,
    url_prefix: str,
    identifier: str,
    label: str,
    name: str,
    description: str,
    entity_schema: Optional[schema.CreateEntity] = None,
) -> None:
    """Update entity."""
    if entity_schema is None:
        entity_schema = schema.CreateEntity(
            name=name,
            label=label,
            description=description,
        )

    data = schema.UpdateEntityRequest(
        entity=entity_schema,
    )

    util.put_and_process(
        ctx,
        f"{url_prefix}/{identifier}",
        json=data.dict(exclude_none=True, by_alias=True),
    )


def get_entity_info(ctx: typer.Context, url_prefix: str, identifier: str) -> None:
    """Get entity info."""
    util.get_and_process(ctx, f"{url_prefix}/{identifier}/info")


def update_entity_info(
    ctx: typer.Context,
    url_prefix: str,
    identifier: str,
    owner: str,
    contacts: List[str],
    links: List[str],
) -> None:
    """Update entity info."""
    data = schema.EntityInfo(
        owner=owner,
        contact_ids=contacts,
        links=links,
    )
    util.put_and_process(
        ctx,
        f"{url_prefix}/{identifier}/info",
        json=data.dict(exclude_none=True, by_alias=True),
    )


def get_entity_journal(
    ctx: typer.Context,
    url_prefix: str,
    identifier: str,
) -> None:
    """Get entity journal."""
    util.get_and_process(ctx, f"{url_prefix}/{identifier}/journal")


def update_entity_journal(ctx: typer.Context, url_prefix: str, identifier: str, note: str) -> None:
    """Update entity journal note."""
    data = schema.JournalEntry(note=note)
    util.post_and_process(
        ctx,
        f"{url_prefix}/{identifier}/journal",
        json=data.dict(exclude_none=True, by_alias=True),
    )


def get_entity_links(ctx: typer.Context, url_prefix: str, identifier: str) -> None:
    """Get entity links."""
    util.get_and_process(ctx, f"{url_prefix}/{identifier}/link")
