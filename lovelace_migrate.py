#!/usr/bin/env python3

import argparse
import logging
import os
import shutil
import sys
from collections import OrderedDict

import homeassistant.core
from homeassistant.config import find_config_file, get_default_config_dir, load_yaml_config_file
from homeassistant.util import yaml

_LOGGER = logging.getLogger(__name__)
GROUP_CONFIG = None


def convert_all_group(obj_id):
    lovelace = OrderedDict()
    lookup = {
        'all_lights': 'light',
        'all_automations': 'automation',
        'all_devices': 'device_tracker',
        'all_fans': 'fan',
        'all_locks': 'lock',
        'all_covers': 'cover',
        'all_remotes': 'remote',
        'all_switches': 'switch',
        'all_vacuum_cleaners': 'vacuum',
        'all_scripts': 'script',
    }
    if obj_id not in lookup:
        _LOGGER.warning("Unknown group.all_* group 'group.{}'".format(obj_id))
        return None
    lovelace['type'] = 'entity-filter'
    lovelace['card_config'] = {'title': obj_id.replace('_', ' ').title()}
    lovelace['filter'] = [{'domain': lookup[obj_id]}]
    return lovelace


def convert_card(entity_id):
    domain, obj_id = entity_id.split('.')
    if domain == 'group':
        if obj_id not in GROUP_CONFIG:
            if obj_id.startswith('all_'):
                return convert_all_group(obj_id)
            _LOGGER.error("Couldn't find group with entity id {}".format(entity_id))
            return None
        return convert_group(GROUP_CONFIG[obj_id], entity_id)
    elif domain == 'camera':
        return OrderedDict([
            ('type', 'camera-preview'),
            ('entity', entity_id)
        ])
    elif domain == 'history_graph':
        return OrderedDict([
            ('type', 'history-graph'),
            ('entity', entity_id)
        ])
    elif domain == 'media_player':
        return OrderedDict([
            ('type', 'media-control'),
            ('entity', entity_id)
        ])
    elif domain == 'plant':
        return OrderedDict([
            ('type', 'plant-status'),
            ('entity', entity_id)
        ])
    elif domain == 'weather':
        return OrderedDict([
            ('type', 'weather-forecast'),
            ('entity', entity_id)
        ])
    _LOGGER.error("Cannot determine card type for entity id '{}'. Maybe it is unsupported?"
                  "".format(entity_id))
    return None


def convert_group(config, name):
    if config.get('view', False):
        _LOGGER.error("Cannot have view group '{}' inside another group".format(name))
        return None

    lovelace = OrderedDict()
    lovelace['type'] = 'entities'
    if 'name' in config:
        lovelace['title'] = config['name']
    entities = lovelace['entities'] = []
    extra_cards = []
    for entity_id in config.get('entities', []):
        domain, obj_id = entity_id.split('.')
        if domain in ['group', 'media_player', 'camera', 'history_graph',
                      'media_player', 'plant', 'weather']:
            _LOGGER.warning("Cannot have domain '{}' within a non-view group {}! "
                            "I will put it into the parent view-type group.".format(
                domain, name))
            card = convert_card(entity_id)
            if card is not None:
                extra_cards.append(card)
            continue
        entities.append(entity_id)
    return lovelace, extra_cards


def convert_view(config, name):
    lovelace = OrderedDict()
    if 'name' in config:
        lovelace['name'] = config['name']
    if 'icon' in config:
        lovelace['tab_icon'] = config['icon']
    cards = lovelace['cards'] = []
    for entity_id in config.get('entities', []):
        card = convert_card(entity_id)
        if card is None:
            continue
        if isinstance(card, tuple):
            cards.append(card[0])
            cards.extend(card[1])
        else:
            cards.append(card)

    return lovelace


def main():
    global GROUP_CONFIG

    logging.basicConfig(level=logging.INFO)

    try:
        from colorlog import ColoredFormatter
        logging.getLogger().handlers[0].setFormatter(ColoredFormatter(
            "%(log_color)s%(levelname)s %(message)s%(reset)s",
            datefmt="",
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            }
        ))
    except ImportError:
        pass

    parser = argparse.ArgumentParser(
        description="Check Home Assistant configuration.")
    parser.add_argument(
        '-c', '--config',
        default=get_default_config_dir(),
        help="Directory that contains the Home Assistant configuration")

    args = parser.parse_args()

    config_dir = os.path.join(os.getcwd(), args.config)

    hass = homeassistant.core.HomeAssistant()
    hass.config.config_dir = config_dir

    config_path = find_config_file(config_dir)
    config = load_yaml_config_file(config_path)
    GROUP_CONFIG = config['group']
    name = config['homeassistant'].get('name', 'Home')
    lovelace = OrderedDict()
    lovelace['name'] = name
    views = lovelace['views'] = []

    if 'default_view' in GROUP_CONFIG:
        views.append(convert_view(GROUP_CONFIG['default_view'], 'default_view'))

    for name, conf in GROUP_CONFIG.items():
        if name == 'default_view':
            continue
        if not conf.get('view', False):
            continue
        views.append(convert_view(conf, name))

    views.append({
        'name': "All Entities",
        'tab_icon': "mdi:settings",
        'cards': [{
            'type': 'entity-filter',
            'filter': [{}],
            'card_config': {
                'title': 'All Entities'
            }
        }],
    })

    lovelace_path = os.path.join(config_dir, 'ui-lovelace.yaml')
    if os.path.exists(lovelace_path):
        i = 0
        while os.path.exists(lovelace_path + '.bkp.{}'.format(i)):
            i += 1
        bkp_path = lovelace_path + '.bkp.{}'.format(i)
        shutil.move(lovelace_path, bkp_path)
        _LOGGER.error("The lovelace configuration already exists under %s! "
                      "I will move it to %s", lovelace_path, bkp_path)
    with open(lovelace_path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(lovelace) + '\n')
    _LOGGER.info("Successfully migrated lovelace configuration to %s", lovelace_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())