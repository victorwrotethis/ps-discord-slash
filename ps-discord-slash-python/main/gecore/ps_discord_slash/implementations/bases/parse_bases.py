from gecore.ps_discord_slash.implementations.bases.extra_bases import additional_bases
from gecore.ps_discord_slash.implementations.bases.load_bases import load_facilities_file


class BasesParser:

    def __init__(self):
        self.facility_json = load_facilities_file()

    def create_base_list(self) -> {}:
        """"
        Loads facilities from the map region list and transforms it into a string/int pair.
        Facilities that have their base name stripped in the json will get them returned.
        For example: Naum of facility type 2 will get Amp Station appended to it.
        The varieties are: 2 = Amp Station, 3 = Bio Lab, 4 = Tech Plant.
        """
        facilities = self.facility_json['map_region_list']
        bases = parse_bases(facilities)
        bases.update(load_extra_bases())
        return bases


def parse_bases(facilities) -> {}:
    base_dict = {}
    for facility in facilities:
        name = facility['facility_name']
        if 'facility_type_id' in facility:
            if int(facility['facility_type_id']) in [2, 3, 4]:
                name = name + ' ' + facility['facility_type']
        if 'facility_id' in facility:
            base_dict[name] = int(facility['facility_id'])
        else:
            base_dict[name] = -2
    return base_dict


def load_extra_bases() -> []:
    other_bases = additional_bases()
    parsed_extra_bases = parse_bases(other_bases)
    return parsed_extra_bases
