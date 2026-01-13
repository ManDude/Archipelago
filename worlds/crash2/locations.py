from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import Crash2World

level_names = ["Turtle Woods",
               "Snow Go",
               "Hang Eight",
               "The Pits",
               "Crash Dash",
               "Ripper Roo", #Boss 1
               "Snow Biz",
               "Air Crash",
               "Bear It",
               "Crash Crush",
               "The Eel Deal",
               "Komodo Brothers", #Boss 2
               "Plant Food",
               "Sewer or Later",
               "Bear Down",
               "Road to Ruin",
               "Un-Bearable",
               "Tiny Tiger", #Boss 3
               "Hangin' Out",
               "Diggin' It",
               "Cold Hard Crash",
               "Ruination",
               "Bee-Having",
               "Dr. N. Gin", #Boss 4
               "Piston it Away",
               "Rock It",
               "Night Fight",
               "Pack Attack",
               "Spaced Out",
               "Dr. Neo Cortex", #Boss 5
               "Totally Bear",
               "Totally Fly",
 ]

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
# LOCATION_NAME_TO_ID = {
#     "Top Left Room Chest": 1,
#     "Top Middle Chest": 2,
#     "Bottom Left Chest": 3,
#     "Bottom Left Extra Chest": 4,
#     "Bottom Right Room Left Chest": 5,
#     "Bottom Right Room Right Chest": 6,
#     # Location IDs don't need to be sequential, as long as they're unique and greater than 0.
#     "Right Room Enemy Drop": 10,
# }
LOCATION_NAME_TO_ID = {
    "Turtle Woods Crystal": 1,
    "Turtle Woods Clear Gem (Box Gem)": 2,
    "Turtle Woods Blue Gem": 3,

    "Snow Go Crystal": 4,
    "Snow Go Clear Gem (Box Gem)": 5,
    "Snow Go Red Gem": 6,

    "Hang Eight Crystal": 7,
    "Hang Eight Clear Gem (Box Gem)": 8,
    "Hang Eight Clear Gem (Timer)": 9,

    "The Pits Crystal": 10,
    "The Pits Clear Gem (Box Gem)": 11,

    "Crash Dash Crystal": 12,
    "Crash Dash Clear Gem (Box Gem)": 13,

    "Ripper Roo Defeated": 14,

    "Snow Biz Crystal": 15,
    "Snow Biz Clear Gem (Box Gem)": 16,

    "Air Crash Crystal": 17,
    "Air Crash Clear Gem (Box Gem)": 18,
    "Air Crash Clear Gem (Death Route)": 19,

    "Bear It Crystal": 20,
    "Bear It Clear Gem (Box Gem)": 21,

    "Crash Crush Crystal": 22,
    "Crash Crush Clear Gem (Box Gem)": 23,

    "The Eel Deal Crystal": 24,
    "The Eel Deal Clear Gem (Box Gem)": 25,
    "The Eel Deal Green Gem": 26,

    "Komodo Brothers Defeated": 27,

    "Plant Food Crystal": 28,
    "Plant Food Clear Gem (Box Gem)": 29,
    "Plant Food Yellow Gem": 30,

    "Sewer or Later Crystal": 31,
    "Sewer or Later Clear Gem (Box Gem)": 32,
    "Sewer or Later Clear Gem (Yellow Gem Path)": 33,

    "Bear Down Crystal": 34,
    "Bear Down Clear Gem (Box Gem)": 35,

    "Road to Ruin Crystal": 36,
    "Road to Ruin Clear Gem (Box Gem)": 37,
    "Road to Ruin Clear Gem (Death Route)": 38,

    "Un-Bearable Crystal": 39,
    "Un-Bearable Clear Gem (Box Gem)": 40,

    "Tiny Tiger Defeated": 41,

    "Hangin' Out Crystal": 42,
    "Hangin' Out Clear Gem (Box Gem)": 43,

    "Diggin' It Crystal": 44,
    "Diggin' It Clear Gem (Box Gem)": 45,
    "Diggin' It Clear Gem (Death Route)": 46,

    "Cold Hard Crash Crystal": 47,
    "Cold Hard Crash Clear Gem (Box Gem)": 48,
    "Cold Hard Crash Clear Gem (Death Route)": 49,

    "Ruination Crystal": 50,
    "Ruination Clear Gem (Box Gem)": 51,
    "Ruination Clear Gem (Green Gem Path)": 52,

    "Bee-Having Crystal": 53,
    "Bee-Having Clear Gem (Box Gem)": 54,
    "Bee-Having Purple Gem": 55,

    "Dr. N. Gin Defeated": 56,

    "Piston it Away Crystal": 57,
    "Piston it Away Clear Gem (Box Gem)": 58,
    "Piston it Away Clear Gem (Death Route)": 59,

    "Rock It Crystal": 60,
    "Rock It Clear Gem (Box Gem)": 61,

    "Night Fight Crystal": 62,
    "Night Fight Clear Gem (Box Gem)": 63,
    "Night Fight Clear Gem (Death Route)": 64,

    "Pack Attack Crystal": 65,
    "Pack Attack Clear Gem (Box Gem)": 66,

    "Spaced Out Crystal": 67,
    "Spaced Out Clear Gem (Box Gem)": 68,
    "Spaced Out Clear Gem (All Colored Gems Path)": 69,

    #"Dr. Neo Cortex Defeated": 70,

    "Totally Bear Clear Gem (Box Gem)": 71,
    "Totally Fly Clear Gem (Box Gem)": 72,
}



# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class Crash2Location(Location):
    game = "Crash2"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: Crash2World) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: Crash2World) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    # overworld = world.get_region("Overworld")
    # top_left_room = world.get_region("Top Left Room")
    # bottom_right_room = world.get_region("Bottom Right Room")
    # right_room = world.get_region("Right Room")

    locations = LOCATION_NAME_TO_ID.keys()
    for name in level_names:
        region = world.get_region(name)
        for location in locations:
            if name in location:
                region.locations.append(Crash2Location(world.player, location, world.location_name_to_id[location], region))

    # region = world.get_region("Dr. Neo Cortex")
    # location = ""
    # region.locations.append(Crash2Location(world.player, location, world.location_name_to_id[location], region))

    # One way to create locations is by just creating them directly via their constructor.
    # bottom_left_chest = APQuestLocation(
    #     world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    # )
    #
    # # You can then add them to the region.
    # overworld.locations.append(bottom_left_chest)
    #
    # # A simpler way to do this is by using the region.add_locations helper.
    # # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # # You also need to pass your overridden Location class.
    # bottom_right_room_locations = get_location_names_with_ids(
    #     ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    # )
    # bottom_right_room.add_locations(bottom_right_room_locations, APQuestLocation)
    #
    # top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    # top_left_room.add_locations(top_left_room_locations, APQuestLocation)
    #
    # right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    # right_room.add_locations(right_room_locations, APQuestLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    # top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    # else:
    #     overworld.add_locations(top_middle_room_locations, APQuestLocation)
    #
    # # Locations may exist only if the player enables certain options.
    # # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    # if world.options.extra_starting_chest:
    #     # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
    #     # exist, it must still always be present in the world's location_name_to_id.
    #     # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
    #     bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
    #     overworld.add_locations(bottom_left_extra_chest, APQuestLocation)


def create_events(world: Crash2World) -> None:

    world.get_region("Dr. Neo Cortex").add_event(
        "Dr. Neo Cortex Defeated", "Victory", location_type=Crash2Location, item_type=items.Crash2Item
    )
    # # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # # In our case, the player must press a button in the top left room to open the final boss door.
    # # AP has something for this purpose: "Event locations" and "Event items".
    # # An event location is no different than a regular location, except it has the address "None".
    # # It is treated during generation like any other location, but then it is discarded.
    # # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    # top_left_room = world.get_region("Top Left Room")
    # final_boss_room = world.get_region("Final Boss Room")
    #
    # # One way to create an event is simply to use one of the normal methods of creating a location.
    # button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    # top_left_room.locations.append(button_in_top_left_room)
    #
    # # We then need to put an event item onto the location.
    # # An event item is an item whose code is "None" (same as the event location's address),
    # # and whose classification is "progression". Item creation will be discussed more in items.py.
    # # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # # it is common practice to create the item when creating the location.
    # # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # # we'll create both the event location and the event item in our locations.py code.
    # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    # button_in_top_left_room.place_locked_item(button_item)
    #
    # # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # # Luckily, we have another event we want to create: The Victory event.
    # # We will use this event to track whether the player can win the game.
    # # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    # final_boss_room.add_event(
    #     "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    # )
    #
    # # If you create all your regions and locations line-by-line like this,
    # # the length of your create_regions might get out of hand.
    # # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # # However, it is worth understanding how the actual creation of regions and locations works,
    # # That way, we're not just mindlessly copy-pasting! :)
