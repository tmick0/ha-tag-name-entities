# Home Assistant Tag Name Entities

This is a custom integration that will provide entities of the form `tag_name.xx_xx_xx_xx`,
where the part after the `.` is the tag ID with `-` replaced by `_`.

The state value of these entities is the Name assigned to the tag in the Settings. The states are
automatically be updated whenever tags are added, removed, or renamed.

## Installation

### Manual

Copy `custom_components/tag_name_entities` to your installation's `custom_components` folder.

### HACS

This component is not listed in HACS, but you can add this repo as a custom source to use HACS to install it.

Navigate to HACS -> Integrations -> (3-dots menu) -> Custom Repositories. Specify the repository URL
`https://github.com/tmick0/ha-tag-name-entities.git` and the type `Integration`. You should then be able to
install it.

## Usage

To enable the component, add `tag_name_entities:` to `configuration.yaml`.

To use tag names in automations, retrieve them like `{{ states('tag_name.' + trigger.event.data.tag_id.replace('-','_')) }}`.
