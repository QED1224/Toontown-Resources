###############################################################################
# toontown.py (last updated 03/24/15):
#
# The goal of this module is to simplify common Panda3D tasks
# such as creating cogs, toons and playgrounds (coming soon).
# I've attempted to accomplish this by significantly reducing the
# amount of code involved in these tasks.
#
# This file contains:
#
# 1. load_cog - Returns any traditional cog or boss (as an Actor).
# 2. make_boss - Returns any boss (as an Actor).
# 3. make_cog - Returns any cog (as an Actor).
# 4. Toon - Subclass of Panda3D"s Actor class; expedites creating and editing
#    toons.
# 5. toon_colors - Dictionary which maps color names to their numerical values.
# 6. toon_animation - Returns two (torso and leg) animation dictionaries for a
#    toon.
# 7. cog_animation - Returns an animation dictionary for a cog.
#
# TODO: Fix path issues on Windows (Maybe drop sleeve-matching altogether?).
###############################################################################

from __future__ import with_statement

import fnmatch
import difflib
import os
import re

try:
    import cPickle as pickle
except ImportError:
    import pickle

from direct.actor.Actor import Actor
from panda3d.core import Filename as pfile, getModelPath
import direct.directbase.DirectStart

__author__ = "QED"
__version__ = "0.0.6"
__status__ = "Prototype"

MODEL_PATH = getModelPath().getDirectories()[-1].toOsSpecific()

cog_dict = {
    "VP":
        ["sell", "sell"],
    "Mr. Hollywood":
        ["yesman", "A", "A", "sell", "", (7.0 / 6.06)],
    "The Mingler":
        ["twoface", "A", "A", "sell", "mingler", (5.75 / 6.06)],
    "Two-Face":
        ["twoface", "A", "A", "sell", "", (4.25 / 6.06)],
    "Mover & Shaker":
        ["movershaker", "B", "B", "sell", "", (4.375 / 5.29)],
    "Gladhander":
        ["gladhander", "C", "C", "sell", "", (4.75 / 4.14)],
    "Name Dropper":
        ["numbercruncher", "A", "A", "sell", "name-dropper", (4.35 / 6.06)],
    "Telemarketer":
        ["telemarketer", "B", "B", "sell", "", (3.75 / 5.29)],
    "Cold Caller":
        ["coldcaller", "C", "C", "sell", "", (3.5 / 4.14)],
    "CFO":
        ["cash", "cash"],
    "Robber Baron":
        ["yesman", "A", "A", "cash", "robber-baron", (7.0 / 6.06)],
    "Loan Shark":
        ["loanshark", "B", "B", "cash", "", (6.5 / 5.29)],
    "Moneybags":
        ["moneybags", "C", "C", "cash", "", (5.3 / 4.14)],
    "Number Cruncher":
        ["numbercruncher", "A", "A", "cash", "", (5.25 / 6.06)],
    "Bean Counter":
        ["beancounter", "B", "B", "cash", "", (4.4 / 5.29)],
    "Tightwad":
        ["tightwad", "C", "C", "cash", "", (4.5 / 4.14)],
    "Penny Pincher":
        ["pennypincher", "A", "A", "cash", "", (3.55 / 6.06)],
    "Short Change":
        ["coldcaller", "C", "C", "cash", "", (3.6 / 4.14)],
    "CJ":
        ["law", "law"],
    "Bigwig":
        ["bigwig", "A", "A", "law", "", (7 / 6.06)],
    "Legal Eagle":
        ["legaleagle", "A", "A", "law", "", (7.125 / 6.06)],
    "Spin Doctor":
        ["telemarketer", "B", "B", "law", "spin-doctor", (5.65 / 5.29)],
    "Backstabber":
        ["backstabber", "A", "A", "law", "", (4.5 / 6.06)],
    "Ambulance Chaser":
        ["ambulancechaser", "B", "B", "law", "", (4.35 / 5.29)],
    "Double Talker":
        ["twoface", "A", "A", "law", "double-talker", (4.25 / 6.06)],
    "Bloodsucker":
        ["movershaker", "B", "B", "law", "blood-sucker", (4.375 / 5.29)],
    "Bottomfeeder":
        ["tightwad", "C", "C", "law", "bottom-feeder", (4 / 4.14)],
    "CEO":
        ["boss", "boss"],
    "The Big Cheese":
        ["bigcheese", "A", "A", "boss", "", (7 / 6.06)],
    "Corporate Raider":
        ["flunky", "C", "C", "boss", "corporate-raider", (6.75 / 4.14)],
    "Head Hunter":
        ["headhunter", "A", "A", "boss", "", (6.5 / 6.06)],
    "Downsizer":
        ["beancounter", "B", "B", "boss", "", (4.5 / 5.29)],
    "Micromanager":
        ["micromanager", "C", "C", "boss", "", (2.5 / 4.14)],
    "Yesman":
        ["yesman", "A", "A", "boss", "", (4.125 / 6.06)],
    "Pencil Pusher":
        ["pencilpusher", "B", "B", "boss", "", (3.35 / 5.29)],
    "Flunky":
        ["flunky", "C", "C", "boss", "", (4 / 4.14)]
}

"""
A dictionary which allows for the use of actual color names. For example,

from toontown import toon_colors as tcolors

.setColor(tcolors["Red"])
"""
toon_colors = {
    "Blue": (0.191, 0.563, 0.773, 1.0),
    "Periwinkle": (0.559, 0.59, 0.875, 1.0),
    "Sea Green": (0.242, 0.742, 0.516, 1.0),
    "Peach": (1.0, 0.82, 0.7, 1.0),
    "Purple": (0.547, 0.281, 0.75, 1.0),
    "Pink": (0.898, 0.617, 0.906, 1.0),
    "Yellow": (0.996, 0.898, 0.32, 1.0),
    "Citrine": (0.855, 0.934, 0.492, 1.0),
    "Orange": (0.992, 0.48, 0.168, 1.0),
    "White": (1.0, 1.0, 1.0, 1.0),
    "Lime Green": (0.551, 0.824, 0.324, 1.0),
    "Red": (1.0, 0.5, 0.5, 1.0),
    "Brown": (0.641, 0.355, 0.27, 1.0),
    "Slate Blue": (0.461, 0.379, 0.824, 1.0),
    "Grey": (0.7, 0.7, 0.8, 1.0),
    "Royal Blue": (0.285, 0.328, 0.727, 1.0),
    "Aqua": (0.348, 0.82, 0.953, 1.0),
    "Coral": (0.832, 0.5, 0.297, 1.0),
    "Green": (0.305, 0.969, 0.402, 1.0),
    "Light Blue": (0.434, 0.906, 0.836, 1.0),
    "Bright Red": (0.934, 0.266, 0.281, 1.0),
    "Lavender": (0.727, 0.473, 0.859, 1.0),
    "Maroon": (0.711, 0.234, 0.438, 1.0),
    "Sienna": (0.57, 0.449, 0.164, 1.0),
    "Black": (0.3, 0.3, 0.35, 1.0),
    "Tan": (0.996, 0.695, 0.512, 1.0),
    "Cream": (0.996, 0.957, 0.598, 1.0),
    "Beige": (1.0, 0.8, 0.6, 1.0)
}


def load_cog(cog_name, skelecog=False, path=""):
    """Return any traditional cog as an Actor.

    Args:
        cog_name (str): The name of the desired cog.
        skelecog (bool, optional): If `True`, a skelecog will be returned.
          Defaults to `False`.
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.

    Examples:
        from toontown import load_cog

        Hollywood = load_cog("Mr. Hollywood")
        Hollywood.loop("landing")

        skelecog = load_cog("Legal Eagle", True)
        skelecog.loop("neutral")

        CFO = load_cog("CFO")
        CFO.loop("Ff_neutral")

    Returns:
        An instance of Panda3D's Actor class.

    Note:
        This function also supports name matching; that is,

        Hollywood = load_cog("hollywood")

        is the same as

        Hollywood = load_cog("Mr. Hollywood")
    """
    cog_names = cog_dict.keys()
    if cog_name not in cog_names:
        if difflib.get_close_matches(cog_name, cog_names):
            cog_name = difflib.get_close_matches(cog_name, cog_names)[0]
        else:
            for name in cog_names:
                if cog_name.lower() in name.lower():
                    cog_name = name

    args = cog_dict[cog_name]

    if cog_name in ("VP", "CFO", "CJ", "CEO"):
        args.insert(2, path)
        cog = make_boss(*args)
    elif skelecog:
        cog = make_skelecog(args[1], args[3], path)
        cog.setScale(cog_dict[cog_name][5])
    else:
        args.insert(5, path)
        cog = make_cog(*args[0:6])
        cog.setScale(cog_dict[cog_name][6])
    return cog


def make_boss(head, torso, path=""):
    """Return any cog boss as an Actor.

    Args:
        head (str): The name of the boss' suit to be used for its head.
        torse (str): The name of the boss' suit to be used for its torso.
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.

    Examples:
        from toontown import make_boss

        CFO = make_boss("cash", "cash")
        CFO.loop("Ff_neutral")

    Returns:
        An instance of Panda3D's Actor class.
    """
    if path:
        path = pfile.fromOsSpecific("%s/" % path).getFullpath()

    boss_dict = {
        "sell": "phase_9/models/char/sellbotBoss",
        "cash": "phase_10/models/char/cashbotBoss",
        "law": "phase_11/models/char/lawbotBoss",
        "boss": "phase_12/models/char/bossbotBoss"
    }

    head_dict, torso_dict, legs_dict = cog_animation("Boss", path)

    animation = {
        "head": head_dict,
        "torso": torso_dict,
        "legs": legs_dict
    }

    parts = {
        "head": "%s%s-head-zero.bam" % (path, boss_dict[head]),
        "torso": "%s%s-torso-zero.bam" % (path, boss_dict[torso]),
        "legs": "%sphase_9/models/char/bossCog-legs-zero.bam" % path
    }

    boss = Actor(parts, animation)
    treads = loader.loadModel(
        "%sphase_9/models/char/bossCog-treads.bam" % path
    )
    boss.attach("head", "torso", "joint34")
    boss.attach("torso", "legs", "joint_pelvis")
    treads.reparentTo(boss.find("**/joint_axle"))
    boss.reparentTo(render)
    return boss


def make_skelecog(suit_style, suit_name, path=""):
    """Return a skelecog version of any traditional cog as an Actor.

    Args:
        suit_style (str): The letter representing the suit style
            ("A", "B" or "C").
        suit_name (str): The name of the boss' suit.
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.

    Examples:
        from toontown import make_skelecog

        skelecog = make_skelecog("A", "cash")
        skelecog.loop("neutral")

    Returns:
        An instance of Panda3D's Actor class.
    """
    if path:
        path = pfile.fromOsSpecific("%s/" % path).getFullpath()

    icon_dict = {
        "sell": ("Sales", (0.843, 0.745, 0.745, 1.0)),
        "cash": ("Money", (0.749, 0.769, 0.749, 1.0)),
        "law": ("Legal", (0.749, 0.776, 0.824, 1.0)),
        "boss": ("Corp", (0.863, 0.776, 0.769, 1.0))
    }

    animation_dict = cog_animation(suit_style, path)

    skelecog = Actor(
        "%sphase_5/models/char/cog%s_robot-zero.bam" % (path, suit_style),
        animation_dict
    )

    if icon_dict[suit_name.lower()][0] == "Corp":
        tie = loader.loadTexture(
            "%sphase_5/maps/cog_robot_tie_boss.jpg" % path
        )
    else:
        idict = icon_dict[suit_name][0].lower()
        tie = loader.loadTexture(
            "%sphase_5/maps/cog_robot_tie_%s.jpg" % (path, idict)
        )
    skelecog.findAllMatches("**/tie").setTexture(tie, 1)

    icons = loader.loadModel("%sphase_3/models/gui/cog_icons.bam" % path)
    icon = icons.find(
        "**/%sIcon" % icon_dict[suit_name][0]
    ).copyTo(skelecog.find("**/joint_attachMeter"))
    icon.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
    icon.setColor(icon_dict[suit_name.lower()][1])
    icons.removeNode()

    skelecog.reparentTo(render)
    return skelecog


def make_cog(head, head_style, suit_style, suit_name, head_text="", path=""):
    """Return a skelecog version of any traditional cog as an Actor.

    Args:
        head (str): The name of the cog.
        head_style (str): The letter representing the suit style
            ("A", "B" or "C").
        suit_style (str): The letter representing the suit style
            ("A", "B" or "C").
        suit_name (str): The name of the suit.
        head_text (str, optional): The name of a head texture.
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.

    Examples:
        from toontown import make_cog

        Hollywood = make_cog("yesman", "A", "A", "sell")
        Hollywood.loop("landing")

        RobberBaron = make_cog("yesman", "A", "A", "cash", "robber-baron")
        RobberBaron.loop("walk")

        SpinDoctor = make_cog("telemarketer", "B", "B", "law", "spin-doctor")
        SpinDoctor.loop("throw-paper")

    Returns:
        An instance of Panda3D's Actor class.
    """

    if path:
        path = pfile.fromOsSpecific("%s/" % path).getFullpath()

    abrv = {
        "sell": (
            "s", (0.95, 0.75, 0.95, 1.0),
            "Sales", (0.843, 0.745, 0.745, 1.0)
        ),
        "cash": (
            "m", (0.65, 0.95, 0.85, 1.0),
            "Money", (0.749, 0.769, 0.749, 1.0)
        ),
        "law": (
            "l", (0.75, 0.75, 0.95, 1.0),
            "Legal", (0.749, 0.776, 0.824, 1.0)
        ),
        "boss": (
            "c", (0.95, 0.75, 0.75, 1.0),
            "Corp", (0.863, 0.776, 0.769, 1.0)
        )
    }

    cog_color = {
        "coldcaller": ((0.75, 0.75, 0.95, 1.0), ""),
        "pennypincher": ((1.0, 0.5, 0.6, 1.0), ""),
        "legaleagle": ((0.25, 0.25, 0.5, 1.0), ""),
        "telemarketer": ((0.5, 0.8, 0.75, 1.0), "spin-doctor"),
        "movershaker": ((0.95, 0.95, 1.0, 1.0), "blood-sucker"),
        "bigcheese": ((0.75, 0.95, 0.75, 1.0), ""),
        "flunky": ((0.85, 0.55, 0.55, 1.0), "corporate-raider")
    }

    blazer = loader.loadTexture(
        "%sphase_3.5/maps/%s_blazer.jpg" % (path, abrv[suit_name][0])
    )
    sleeve = loader.loadTexture(
        "%sphase_3.5/maps/%s_sleeve.jpg" % (path, abrv[suit_name][0])
    )
    leg = loader.loadTexture(
        "%sphase_3.5/maps/%s_leg.jpg" % (path, abrv[suit_name][0])
    )

    animation_dict = cog_animation(suit_style, path)

    if suit_style in ("A", "B"):
        cog = Actor(
            "%sphase_3.5/models/char/suit%s-mod.bam" % (path, suit_style),
            animation_dict
        )
    else:
        cog = Actor(
            "%sphase_3.5/models/char/suitC-mod.bam" % path, animation_dict
        )

    if head_style in ("A", "B"):
        head_model = loader.loadModel(
            "%sphase_4/models/char/suit%s-heads.bam" % (path, head_style)
        )
    else:
        head_model = loader.loadModel(
            "%sphase_3.5/models/char/suitC-heads.bam" % path
        )

    cog_head = head_model.find("**/%s" % head)
    joint_head = cog.find("**/joint_head")
    cog_head.reparentTo(joint_head)

    if head in cog_color.keys() and head_text == cog_color[head][1]:
        cog.find("**/hands").setColor(cog_color[head][0])
    else:
        cog.find("**/hands").setColor(abrv[suit_name][1])

    if head_text and head_text not in ("bottom-feeder", "corporate-raider"):
        head_texture = loader.loadTexture(
            "%sphase_4/maps/%s.jpg" % (path, head_text)
        )
        cog.findAllMatches("**/%s" % head).setTexture(head_texture, 1)
    elif head_text in ("bottom-feeder", "corporate-raider"):
        head_texture = loader.loadTexture(
            "%sphase_3.5/maps/%s.jpg" % (path, head_text)
        )
        cog.findAllMatches("**/%s" % head).setTexture(head_texture, 1)

    if head == "flunky" and not head_text:
        head_model.find("**/glasses").reparentTo(cog_head)

    icons = loader.loadModel("%sphase_3/models/gui/cog_icons.bam" % path)
    icon = icons.find(
        "**/%sIcon" % abrv[suit_name][2]
    ).copyTo(cog.find("**/joint_attachMeter"))
    icon.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
    icon.setColor(abrv[suit_name][3])
    icons.removeNode()

    cog.find("**/legs").setTexture(leg, 1)
    cog.find("**/torso").setTexture(blazer, 1)
    cog.find("**/arms").setTexture(sleeve, 1)
    cog.reparentTo(render)

    return cog

class Toon(Actor):
    """A wrapper over Panda3D's Actor class designed for working with toons.

    Examples:
        from toontown import Toon

        Flippy = Toon("dog", "m", "n", "n", "m", "m")
        Flippy.set_color("Aqua")
        Flippy.set_shirt(
            "phase_3/maps/desat_shirt_4.jpg", color=(1.25,0.49,0.02)
        )
        Flippy.set_bottom("phase_3/maps/desat_shorts_10.jpg", (0.55,0.27,0.63))
        Flippy.loop("walk")
    """
    def __init__(self, species, gender, head, features, torso_size, legs_size, path=""):
        """
        Args:
            species (str): "cat", "dog", "duck", "mouse", "pig", "rabbit",
                "bear", "horse" or "monkey".
            gender (str): "m" (male) or "f" (female).
            head (str): "n" (normal) or "l" (long).
            features (str): "n" (normal) or "l" (long).
            torso_size (str): "s" (small), "m" (medium) or "l" (long).
            legs_size (str): "s" (small), "m" (medium) or "l" (long).
            path (str, optional): The file path to the Toontown phase files.
                Defaults to Panda3D's search path.
        """
        global MODEL_PATH
        if path:
            self.path = pfile.fromOsSpecific("%s/" % path).getFullpath()
        else:
            self.path = pfile.fromOsSpecific("%s/" % MODEL_PATH).getFullpath()
        self.species = species
        self.gender = gender
        self.dimensions = torso_size, legs_size
        self.__make_actor(
            species, gender, head, features, torso_size, legs_size
        )
        Actor.__init__(self, self.parts, self.animation)
        self.__initialize_actor()

    def set_color(self, color, *parts):
        """Sets the toon"s color based on these arguments:

        Args:
            color (str): any color in the dictionary toon_colors directly
                referenced by its name (i.e. "blue").
            parts (str, optional): "head", "arms" or "legs" specifying a body
                part(s) to be changed.

        Examples:
            # sets the entire toon to red.
            my_toon.set_color("red")

            # only sets the toon's arms and legs to red.
            my_toon.set_color("red", "arms", "legs")

            # only sets the toon's head to red.
            my_toon.set_color("red", "head")
        """
        toon_parts = [
            ("**/head*", "**/head-front"),
            ("**/neck", "**/arms"),
            ("**/legs", "**/feet"),
            ("**/*ears*", "")
        ]
        color = color.title()

        if self.species.lower() in ("dog", "horse", "monkey"):
            # "ears" must be last in the toon_parts list.
            toon_parts.remove(toon_parts[-1])
        if parts:
            match = [
                x for x in toon_parts for y in parts if y in x[0] or y in x[1]
            ]
        else:
            match = toon_parts

        for each in match:
            self.findAllMatches(each[0]).setColor(toon_colors[color])
            if each[1]:
                self.findAllMatches(each[1]).setColor(toon_colors[color])

    def set_shirt(self, shirt_path, sleeve_path="", color=None):
        """Sets the toon's shirt.

        Args:
            shirt_path (str): the file path to the desired shirt.

            sleeve_path (str, optional): the file path to the desired sleeve.
                If not provided, the function will use the best match.

            color (str, tuple, optional): a color to set the shirt to.
                The value of color may be either a string in toon_colors
                (e.g, "blue") or a tuple representing a color
                (e.g, (0.55, 0.27, 0.63)).

        Examples:
            Case 1: One argument
            my_toon.set_shirt("phase_4/maps/tt_t_chr_avt_shirt_fishing04.jpg")

            Case 2: Two arguments
            my_toon.set_shirt(
                "phase_3/maps/desat_shirt_4.jpg", color=(1.25,0.49,0.02)
            )

            or

            Flippy.set_shirt(
                "phase_3/maps/desat_shirt_4.jpg",
                "phase_3/maps/desat_sleeve_4.jpg"
            )

            Case 3: Three arguments
            my_toon.set_shirt(
                "phase_3/maps/desat_shirt_4.jpg",
                "phase_3/maps/desat_sleeve_4.jpg",
                (1.25,0.49,0.02)
            )
        """
        special_cases = {
            "PJBlueBanana2.jpg": "PJSleeveBlue.jpg",
            "PJRedHorn2.jpg": "PJSleeveRed.jpg",
            "PJGlasses2.jpg": "JSleevePurple.jpg",
            "shirtMale4B.jpg": "StPats_sleeve.jpg",
            "tt_t_chr_avt_shirt_mostCogsDefeated03.jpg": "tt_t_chr_avt_shirtSleeve_mostCogsDefeated02.jpg",
            "tt_t_chr_avt_shirt_mostCogsDefeated04.jpg": "tt_t_chr_avt_shirtSleeve_mostCogsDefeated03.jpg",
            }

        shirt = loader.loadTexture(self.path + shirt_path)

        if sleeve_path:
            sleeves = loader.loadTexture(self.path + sleeve_path)
        else:
            shirt_match = shirt_path.split("/")[-1]
            path = os.path.join(self.path, *shirt_path.split("/")[0:2])

            if shirt_match in special_cases.keys():
                sys_path = os.path.join(path, special_cases[shirt_match])
                sleeve_path = pfile.fromOsSpecific(sys_path).getFullpath()
                sleeves = loader.loadTexture(sleeve_path)
            else:
                if re.search(r"shirt", shirt_match, re.I):
                    sleeve_path = re.sub("(?i)shirt", "sleeve", shirt_match)
                else:
                    index = shirt_match.find(".")
                    sleeve_path = shirt_match[:index] + "_sleeve" + shirt_match[index:]

                if re.search(r"\d+", sleeve_path):
                    num = int(re.findall(r"\d+", sleeve_path)[-1])
                else:
                    num = ""

                match_list = []
                test_num = best_num = 4
                for each in os.listdir(path):
                    if re.search(r"sleeve", each, re.I):
                        if re.search(r"\d+", each):
                            test_num = int(re.findall(r"\d+", each)[-1])
                        if str(num) in each or abs(test_num - num) < best_num:
                            match_list.append(each)
                matches = difflib.get_close_matches(sleeve_path, match_list)

                sleeve_path = pfile.fromOsSpecific(
                    os.path.join(self.path, path, matches[0])
                ).getFullpath()
                sleeves = loader.loadTexture(sleeve_path)

        self.find("**/torso-top").setTexture(shirt, 1)
        self.find("**/sleeves").setTexture(sleeves, 1)

        if color:
            if type(color) == type(str()):
                color = color.title()
                self.find("**/torso-top").setColor(toon_colors[color])
                self.find("**/sleeves").setColor(toon_colors[color])
            else:
                self.find("**/torso-top").setColor(*color)
                self.find("**/sleeves").setColor(*color)

    def set_bottom(self, bottom_path, color=None):
        """Sets the toon"s skirt or shorts.

        Args:
            bottom_path (str): the file path to the desired skirt/shorts.
            color (str, tuple, optional): a color to set the shirt to.
                The value of color may be either a string in toon_colors
                (e.g, "blue") or a tuple repsenting a color
                (e.g, (0.55, 0.27, 0.63)).

        Examples:
            my_toon.set_bottom("phase_4/maps/tt_t_chr_avt_shorts_golf1.jpg")
        """
        bottom = loader.loadTexture(self.path + bottom_path)
        self.find("**/torso-bot").setTexture(bottom, 1)

        if color:
            if type(color) == type(str()):
                color = color.title()
                self.find("**/torso-bot").setColor(toon_colors[color])
            else:
                self.find("**/torso-bot").setColor(*color)

    def get_color_names(self):
        """Returns a list of all available color names.
        """
        return toon_colors.keys()

    def __initialize_actor(self):
        """Initialize the Actor to a plain, white default state.
        """
        self.attach("head", "torso", "def_head")
        self.attach("torso", "legs", "joint_hips")
        self.reparentTo(render)

        self.find("**/boots_short").removeNode()
        self.find("**/boots_long").removeNode()
        self.find("**/shoes").removeNode()
        self.find("**/hands").setColor(toon_colors["White"])
        self.set_color("White")

        if self.gender == "f":
            eyelashes = loader.loadModel(
                "%sphase_3/models/char/%s-lashes.bam" % (self.path, self.species)
            )
            eyelashes.find("**/closed-long").removeNode()
            eyelashes.find("**/closed-short").removeNode()
            eyelashes.find("**/open-%s" % self.head_remove).removeNode()
            eyelashes.reparentTo(self.find("**/eyes*"))

    def __make_actor(self, species, gender, head, features, torso_size, legs_size):
        """Generates the parts needed to contruct an Actor.
        """
        if species == "mouse":
            features = "n"

        dog_head = {"nn": "m_skirt", "nl": "s_shorts", "ln": "m_shorts", "ll": "l_shorts"}
        gender_dict = {"m": "shorts", "f": "skirt"}
        features_dict = {"n": ("short", "long"), "l": ("long", "short")}
        phase3 = "phase_3/models/char/tt_a_chr_dg"

        torso_animations, leg_animations = toon_animation(torso_size, legs_size, gender, self.path)

        torso_model = "%s%s%s_%s_torso_1000.bam" % (self.path, phase3, torso_size, gender_dict[gender])
        legs_model =  "%s%s%s_shorts_legs_1000.bam" % (self.path, phase3, legs_size)

        self.head_keep = features_dict[head][0]
        self.head_remove = features_dict[head][1]
        self.features_keep = features_dict[features][0]
        self.features_remove = features_dict[features][1]

        if species == "dog":
            head_model = loader.loadModel("%s%s%s_head_1000.bam" % (self.path, phase3, dog_head[head + features]))
        else:
            head_model = loader.loadModel("%sphase_3/models/char/%s-heads-1000.bam" % (self.path, species))

            unwanted = head_model.findAllMatches("**/*%s*" % self.head_remove)
            muzzles = head_model.findAllMatches("**/*muzzle*")
            ears = head_model.findAllMatches("**/*ears*")

            if species == "rabbit" and self.head_keep != self.features_keep:
                parts = list(unwanted) + list(muzzles) + list(ears)
                keep_ears = head_model.find("**/ears-%s" % self.features_keep)
                keep_muzzle = head_model.find("**/*muzzle-%s*neutral" % self.features_remove)
            else:
                parts = list(unwanted) + list(muzzles)

            for part in parts:
                if species == "rabbit" and self.head_keep != self.features_keep:
                    if not any(x in str(part) for x in ["ears", "muzzle"]):
                        part.removeNode()
                    elif "muzzle" in str(part) and part != keep_muzzle:
                            part.removeNode()
                    elif "ears" in str(part) and part != keep_ears:
                            part.removeNode()
                else:
                    if not all(x in str(part) for x in ["muzzle", "neutral", self.features_keep]):
                        part.removeNode()

        self.parts = {"head": head_model, "torso": torso_model, "legs": legs_model}
        self.animation = {"torso": torso_animations, "legs": leg_animations}


def toon_animation(torso_size, legs_size, gender, path=""):
    """Returns two toon animation dictionaries.

    Args:
        torso_size (str): "s" (small), "m" (medium) or "l" (large).
        legs_size (str): "s" (small), "m" (medium) or "l" (large).
        gender (str): "m" (male) or "f" (female).
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.
    Note:
        After creating the dictionaries, this function will create a
        directory (on the model path) called "generatedAnim," which will
        store the animation dictionaries associated with each toon combination.
        This means that it will not repeatedly create each dictionary -- it
        will only do it one time per combination.

    Examples:
        from toontown import toon_animation

        torso_animations, leg_animations = toon_animation("s", "l", "m")
    """
    if not path:
        path = MODEL_PATH
    else:
        path = pfile.fromOsSpecific(path).toOsSpecific()

    torso_size = torso_size.lower()
    legs_size = legs_size.lower()
    gender = gender.lower()

    match = torso_size + legs_size + gender + ".txt"
    if not os.path.isdir(os.path.join(path, "generatedAnim")):
        os.makedirs(os.path.join(path, "generatedAnim"))
    gpath = os.path.join(path, "generatedAnim", match)
    if os.path.exists(gpath):
        with open(gpath, "rb") as fp:
            try:
                return pickle.load(fp)
            except:
                print("Caught Exception: replacing file...")

    abrv = {"s": "dgs", "m": "dgm", "l": "dgl"}
    gender_dict = {"m": "shorts", "f": "skirt"}
    phases = ["3", "3.5", "4", "5", "5.5", "6", "9", "10"]

    torso_size = abrv[torso_size]
    legs_size = abrv[legs_size]
    gender = gender_dict[gender]

    torso_match = "tt_a_chr_%s_%s_torso_" % (torso_size, gender)
    legs_match = "tt_a_chr_%s_shorts_legs_" % legs_size

    torso_dict = {}
    legs_dict = {}

    for num in phases:
        location = os.path.join(path, "phase_" + num, "models", "char")
        for bam in os.listdir(location):
            if fnmatch.fnmatch(bam, torso_match + "*"):
                key1 = bam[len(torso_match):-len(".bam")]
                torso_dict[key1] = str(
                    pfile.fromOsSpecific(os.path.join(location, bam))
                )
            if fnmatch.fnmatch(bam, legs_match + "*"):
                key2 = bam[len(legs_match):-len(".bam")]
                legs_dict[key2] = str(
                    pfile.fromOsSpecific(os.path.join(location, bam))
                )

    with open(gpath, "wb") as fp:
        try:
            pickle.dump((torso_dict, legs_dict), fp)
        except:
            pass

    return torso_dict, legs_dict


def cog_animation(cog_type, path=""):
    """Returns an cog animation dictionary.

    Args:
        cog_type (str): "A", "B" or "C".
        path (str, optional): The file path to the Toontown phase files.
            Defaults to Panda3D's search path.

    Note:
        After creating the dictionaries, this function will create a
        directory (on the model path) called "generatedAnim," which will
        store the animation dictionaries associated with each cog type
        (A, B, C and Boss). This means that it will not repeatedly create each
        dictionary -- it will only do it one time per type. The main purpose
        for this is to keep large animation dictionaries out of your .py files.

    Examples:
        from toontown import cog_animation

        animation_dict = cog_animation("C")
    """

    if not path:
        path = MODEL_PATH
    else:
        path = pfile.fromOsSpecific(path).toOsSpecific()

    cog_type = cog_type.capitalize()
    match = cog_type + ".txt"
    if not os.path.isdir(os.path.join(path, "generatedAnim")):
        os.makedirs(os.path.join(path, "generatedAnim"))
    gpath = os.path.join(path, "generatedAnim", match)
    if os.path.exists(gpath):
        with open(gpath, "rb") as fp:
            try:
                return pickle.load(fp)
            except:
                print("Caught Exception: replacing file...")

    if cog_type in ("A", "B", "C"):
        phases = ["3.5", "4", "5", "7", "8", "12"]
        animation_dict = {}
        for num in phases:
            location = os.path.join(path, "phase_" + num, "models", "char")
            for bam in os.listdir(location):
                if fnmatch.fnmatch(bam, "suit" + cog_type + "-*"):
                    key = bam[len("suit" + cog_type + "-"):-len(".bam")]
                    animation_dict[key] = str(
                        pfile.fromOsSpecific(os.path.join(location, bam))
                    )
        generated = animation_dict
    elif cog_type == "Boss":
        phases = ["9"]
        head_dict = {}
        legs_dict = {}
        torso_dict = {}
        for num in phases:
            location = os.path.join(path, "phase_" + num, "models", "char")
            for bam in os.listdir(location):
                if fnmatch.fnmatch(bam, "bossCog-head-*"):
                    key1 = bam[len("bossCog-head-"):-len(".bam")]
                    head_dict[key1] = str(
                        pfile.fromOsSpecific(os.path.join(location, bam))
                    )
                elif fnmatch.fnmatch(bam, "bossCog-torso-*"):
                    key2 = bam[len("bossCog-torso-"):-len(".bam")]
                    torso_dict[key2] = str(
                        pfile.fromOsSpecific(os.path.join(location, bam))
                    )
                elif fnmatch.fnmatch(bam, "bossCog-legs-*"):
                    key3 = bam[len("bossCog-legs-"):-len(".bam")]
                    legs_dict[key3] = str(
                        pfile.fromOsSpecific(os.path.join(location, bam))
                    )
        generated = head_dict, torso_dict, legs_dict
    else:
        raise ValueError("cog_type must be A, B, C or Boss")

    with open(gpath, "wb") as fp:
        try:
            pickle.dump(generated, fp)
        except:
            pass
    return generated
