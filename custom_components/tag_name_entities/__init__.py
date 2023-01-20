from homeassistant.helpers.collection import (
    CollectionChangeSet,
    CHANGE_ADDED,
    CHANGE_REMOVED
)

DOMAIN = "tag_name"

async def async_setup(hass, config):
    hass.data["tag"]["tags"].async_add_change_set_listener(handle_tag_changeset(hass))
    await handle_tag_changeset(hass)([
        CollectionChangeSet(CHANGE_ADDED, item_id, item)
        for item_id, item in hass.data["tag"]["tags"].data.items()
    ])
    return True

def handle_tag_changeset(hass):
    async def fn(change_sets):
        for c in change_sets:
            sanitized_id = c.item_id.replace('-', '_')
            name = f"{DOMAIN}.{sanitized_id}"
            if c.change_type == CHANGE_REMOVED:
                hass.states.async_remove(name)
            else:
                hass.states.async_set(name, c.item.get('name'))
    return fn
