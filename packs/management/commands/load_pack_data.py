# route_214/packs/management/commands/load_pack_data.py

from django.core.management.base import BaseCommand
from packs.models import BoosterPack
import datetime

class Command(BaseCommand):
    help = 'Loads Pokémon booster pack data into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Deleting existing data...'))
        BoosterPack.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing data deleted.'))

        pack_data = [
            # --- Original Series (Wizards of the Coast) ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Base Set", "release_date": "1999-01-09", "price_range": "$500 - $1,500", "price_charting_link": "https://www.pricecharting.com/game/pokemon-base-set/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Jungle", "release_date": "1999-06-16", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-jungle/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Fossil", "release_date": "1999-10-10", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-fossil/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Base Set 2", "release_date": "2000-02-24", "price_range": "$100 - $250", "price_charting_link": "https://www.pricecharting.com/game/pokemon-base-set-2/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Team Rocket", "release_date": "2000-04-24", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-team-rocket/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Gym Heroes", "release_date": "2000-08-14", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-gym-heroes/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Gym Challenge", "release_date": "2000-10-16", "price_range": "$200 - $500", "price_charting_link": "https://www.pricecharting.com/game/pokemon-gym-challenge/booster-pack"},

            # --- Neo Series (Wizards of the Coast) ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Neo Genesis", "release_date": "2000-12-16", "price_range": "$300 - $800", "price_charting_link": "https://www.pricecharting.com/game/pokemon-neo-genesis/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Neo Discovery", "release_date": "2001-06-01", "price_range": "$300 - $800", "price_charting_link": "https://www.pricecharting.com/game/pokemon-neo-discovery/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Neo Revelation", "release_date": "2001-09-21", "price_range": "$300 - $800", "price_charting_link": "https://www.pricecharting.com/game/pokemon-neo-revelation/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Neo Destiny", "release_date": "2002-02-28", "price_range": "$400 - $1,200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-neo-destiny/booster-pack"},

            # --- e-Card Series (Wizards of the Coast) ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Expedition Base Set", "release_date": "2002-09-15", "price_range": "$250 - $700", "price_charting_link": "https://www.pricecharting.com/game/pokemon-expedition/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Aquapolis", "release_date": "2003-01-15", "price_range": "$500 - $1,500", "price_charting_link": "https://www.pricecharting.com/game/pokemon-aquapolis/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Skyridge", "release_date": "2003-05-12", "price_range": "$700 - $2,000", "price_charting_link": "https://www.pricecharting.com/game/pokemon-skyridge/booster-pack"},

            # --- EX Series (Pokémon USA/Nintendo) ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Ruby & Sapphire", "release_date": "2003-06-18", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-ruby-&-sapphire/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Sandstorm", "release_date": "2003-09-18", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-sandstorm/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Dragon", "release_date": "2003-11-24", "price_range": "$200 - $600", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-dragon/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Team Magma vs Team Aqua", "release_date": "2004-03-15", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-team-magma-vs-team-aqua/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Hidden Legends", "release_date": "2004-06-14", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-hidden-legends/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX FireRed & LeafGreen", "release_date": "2004-08-30", "price_range": "$200 - $500", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-firered-&-leafgreen/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Team Rocket Returns", "release_date": "2004-11-08", "price_range": "$250 - $700", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-team-rocket-returns/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Deoxys", "release_date": "2005-02-14", "price_range": "$200 - $600", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-deoxys/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Emerald", "release_date": "2005-05-23", "price_range": "$150 - $450", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-emerald/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Unseen Forces", "release_date": "2005-08-22", "price_range": "$200 - $600", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-unseen-forces/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Delta Species", "release_date": "2005-10-31", "price_range": "$150 - $450", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-delta-species/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Legend Maker", "release_date": "2006-02-13", "price_range": "$120 - $350", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-legend-maker/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Holon Phantoms", "release_date": "2006-05-08", "price_range": "$120 - $350", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-holon-phantoms/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Crystal Guardians", "release_date": "2006-08-30", "price_range": "$120 - $350", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-crystal-guardians/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Dragon Frontiers", "release_date": "2006-11-08", "price_range": "$200 - $600", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-dragon-frontiers/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "EX Power Keepers", "release_date": "2007-02-14", "price_range": "$100 - $300", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ex-power-keepers/booster-pack"},

            # --- Diamond & Pearl Series ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Diamond & Pearl Base Set", "release_date": "2007-05-23", "price_range": "$100 - $250", "price_charting_link": "https://www.pricecharting.com/game/pokemon-diamond-&-pearl/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Diamond & Pearl Mysterious Treasures", "release_date": "2007-08-22", "price_range": "$90 - $200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-diamond-&-pearl-mysterious-treasures/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Diamond & Pearl Secret Wonders", "release_date": "2007-11-07", "price_range": "$90 - $200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-diamond-&-pearl-secret-wonders/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "DP Great Encounters", "release_date": "2008-02-13", "price_range": "$80 - $180", "price_charting_link": "https://www.pricecharting.com/game/pokemon-great-encounters/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "DP Majestic Dawn", "release_date": "2008-07-23", "price_range": "$70 - $160", "price_charting_link": "https://www.pricecharting.com/game/pokemon-majestic-dawn/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Diamond & Pearl Legends Awakened", "release_date": "2008-08-20", "price_range": "$90 - $200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-legends-awakened/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Diamond & Pearl Stormfront", "release_date": "2008-11-05", "price_range": "$100 - $250", "price_charting_link": "https://www.pricecharting.com/game/pokemon-stormfront/booster-pack"},

            # --- Platinum Series ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Platinum", "release_date": "2009-02-11", "price_range": "$100 - $250", "price_charting_link": "https://www.pricecharting.com/game/pokemon-platinum/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Platinum Rising Rivals", "release_date": "2009-05-16", "price_range": "$90 - $200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-rising-rivals/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Platinum Supreme Victors", "release_date": "2009-08-19", "price_range": "$150 - $350", "price_charting_link": "https://www.pricecharting.com/game/pokemon-supreme-victors/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Platinum Arceus", "release_date": "2009-11-04", "price_range": "$90 - $200", "price_charting_link": "https://www.pricecharting.com/game/pokemon-arceus/booster-pack"},

            # --- HeartGold & SoulSilver Series ---
            {"tier": "Tier 2: High-Value Modern", "set_name": "HeartGold & SoulSilver", "release_date": "2010-02-10", "price_range": "$80 - $180", "price_charting_link": "https://www.pricecharting.com/game/pokemon-heartgold-&-soulsilver/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "HS Unleashed", "release_date": "2010-05-12", "price_range": "$70 - $160", "price_charting_link": "https://www.pricecharting.com/game/pokemon-unleashed/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "HS Undaunted", "release_date": "2010-08-18", "price_range": "$70 - $160", "price_charting_link": "https://www.pricecharting.com/game/pokemon-undaunted/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "HS Triumphant", "release_date": "2010-11-03", "price_range": "$60 - $150", "price_charting_link": "https://www.pricecharting.com/game/pokemon-triumphant/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Call of Legends", "release_date": "2011-02-09", "price_range": "$120 - $300", "price_charting_link": "https://www.pricecharting.com/game/pokemon-call-of-legends/booster-pack"},

            # --- Black & White Series ---
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Black & White Base Set", "release_date": "2011-04-25", "price_range": "$70 - $150", "price_charting_link": "https://www.pricecharting.com/game/pokemon-black-&-white/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Emerging Powers", "release_date": "2011-08-31", "price_range": "$60 - $120", "price_charting_link": "https://www.pricecharting.com/game/pokemon-emerging-powers/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Noble Victories", "release_date": "2011-11-16", "price_range": "$70 - $150", "price_charting_link": "https://www.pricecharting.com/game/pokemon-noble-victories/booster-pack"},
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "BW Next Destinies", "release_date": "2012-02-08", "price_range": "$150 - $350", "price_charting_link": "https://www.pricecharting.com/game/pokemon-next-destinies/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Dark Explorers", "release_date": "2012-05-09", "price_range": "$80 - $180", "price_charting_link": "https://www.pricecharting.com/game/pokemon-dark-explorers/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Dragons Exalted", "release_date": "2012-08-15", "price_range": "$80 - $180", "price_charting_link": "https://www.pricecharting.com/game/pokemon-dragons-exalted/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Dragon Vault", "release_date": "2012-10-05", "price_range": "$30 - $70", "price_charting_link": "https://www.pricecharting.com/game/pokemon-dragon-vault/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Boundaries Crossed", "release_date": "2012-11-09", "price_range": "$100 - $250", "price_charting_link": "https://www.pricecharting.com/game/pokemon-boundaries-crossed/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Black & White: Plasma Storm", "release_date": "2013-02-06", "price_range": "$150 - $400", "price_charting_link": "https://www.pricecharting.com/game/pokemon-plasma-storm/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Black & White: Plasma Freeze", "release_date": "2013-05-08", "price_range": "$120 - $300", "price_charting_link": "https://www.pricecharting.com/game/pokemon-plasma-freeze/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Plasma Blast", "release_date": "2013-08-14", "price_range": "$80 - $180", "price_charting_link": "https://www.pricecharting.com/game/pokemon-plasma-blast/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "BW Legendary Treasures", "release_date": "2013-11-06", "price_range": "$70 - $150", "price_charting_link": "https://www.pricecharting.com/game/pokemon-legendary-treasures/booster-pack"},

            # --- XY Series ---
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Base Set", "release_date": "2014-02-05", "price_range": "$20 - $40", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Flashfire", "release_date": "2014-05-07", "price_range": "$30 - $70", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-flashfire/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Furious Fists", "release_date": "2014-08-13", "price_range": "$25 - $50", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-furious-fists/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Phantom Forces", "release_date": "2014-11-05", "price_range": "$25 - $60", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-phantom-forces/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Double Crisis", "release_date": "2015-03-25", "price_range": "$15 - $30", "price_charting_link": "https://www.pricecharting.com/game/pokemon-double-crisis/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Primal Clash", "release_date": "2015-02-04", "price_range": "$20 - $40", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-primal-clash/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Roaring Skies", "release_date": "2015-05-06", "price_range": "$30 - $70", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-roaring-skies/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Ancient Origins", "release_date": "2015-08-12", "price_range": "$25 - $50", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-ancient-origins/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY BREAKthrough", "release_date": "2015-11-04", "price_range": "$20 - $40", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-breakthrough/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Generations", "release_date": "2016-02-22", "price_range": "$20 - $50", "price_charting_link": "https://www.pricecharting.com/game/pokemon-generations/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY BREAKpoint", "release_date": "2016-02-03", "price_range": "$15 - $35", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-breakpoint/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "XY Fates Collide", "release_date": "2016-05-02", "price_range": "$20 - $45", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-fates-collide/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "XY Steam Siege", "release_date": "2016-08-03", "price_range": "$10 - $20", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-steam-siege/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "XY Evolutions", "release_date": "2016-11-01", "price_range": "$15 - $30", "price_charting_link": "https://www.pricecharting.com/game/pokemon-xy-evolutions/booster-pack"},

            # --- Sun & Moon Series ---
            {"tier": "Tier 3: Popular & Strong", "set_name": "Sun & Moon Base Set", "release_date": "2017-02-03", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-sun-&-moon/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Guardians Rising", "release_date": "2017-05-05", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-guardians-rising/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Burning Shadows", "release_date": "2017-08-04", "price_range": "$7 - $12", "price_charting_link": "https://www.pricecharting.com/game/pokemon-burning-shadows/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Shining Legends", "release_date": "2017-10-06", "price_range": "$10 - $25", "price_charting_link": "https://www.pricecharting.com/game/pokemon-shining-legends/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Sun & Moon: Crimson Invasion", "release_date": "2017-11-03", "price_range": "$6 - $10", "price_charting_link": "https://www.pricecharting.com/game/pokemon-crimson-invasion/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Ultra Prism", "release_date": "2018-02-02", "price_range": "$10 - $20", "price_charting_link": "https://www.pricecharting.com/game/pokemon-ultra-prism/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Forbidden Light", "release_date": "2018-05-04", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-forbidden-light/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Celestial Storm", "release_date": "2018-08-03", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-celestial-storm/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Dragon Majesty", "release_date": "2018-09-07", "price_range": "$15 - $30", "price_charting_link": "https://www.pricecharting.com/game/pokemon-dragon-majesty/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Lost Thunder", "release_date": "2018-11-02", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-lost-thunder/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Team Up", "release_date": "2019-02-01", "price_range": "$20 - $40", "price_charting_link": "https://www.pricecharting.com/game/pokemon-team-up/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Detective Pikachu", "release_date": "2019-03-29", "price_range": "$5 - $10", "price_charting_link": "https://www.pricecharting.com/game/pokemon-detective-pikachu/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Unbroken Bonds", "release_date": "2019-05-03", "price_range": "$20 - $40", "price_charting_link": "https://www.pricecharting.com/game/pokemon-unbroken-bonds/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Unified Minds", "release_date": "2019-08-02", "price_range": "$15 - $30", "price_charting_link": "https://www.pricecharting.com/game/pokemon-unified-minds/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Hidden Fates", "release_date": "2019-08-23", "price_range": "$25 - $45", "price_charting_link": "https://www.pricecharting.com/game/pokemon-hidden-fates/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Cosmic Eclipse", "release_date": "2019-11-01", "price_range": "$15 - $30", "price_charting_link": "https://www.pricecharting.com/game/pokemon-cosmic-eclipse/booster-pack"},

            # --- Sword & Shield Series ---
            {"tier": "Tier 4: Standard/Recent", "set_name": "Sword & Shield Base Set", "release_date": "2020-02-07", "price_range": "$4 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-sword-&-shield/booster-pack-base-set"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Rebel Clash", "release_date": "2020-05-01", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-rebel-clash/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Darkness Ablaze", "release_date": "2020-08-14", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-darkness-ablaze/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Champion's Path", "release_date": "2020-09-25", "price_range": "$10 - $25", "price_charting_link": "https://www.pricecharting.com/game/pokemon-champions-path/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Vivid Voltage", "release_date": "2020-11-13", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-vivid-voltage/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Shining Fates", "release_date": "2021-02-19", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-shining-fates/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Battle Styles", "release_date": "2021-03-19", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-battle-styles/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Chilling Reign", "release_date": "2021-06-18", "price_range": "$4 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-chilling-reign/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Evolving Skies", "release_date": "2021-08-27", "price_range": "$10 - $20", "price_charting_link": "https://www.pricecharting.com/game/pokemon-evolving-skies/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Celebrations", "release_date": "2021-10-08", "price_range": "$8 - $15", "price_charting_link": "https://www.pricecharting.com/game/pokemon-celebrations/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Fusion Strike", "release_date": "2021-11-12", "price_range": "$4 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-fusion-strike/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Brilliant Stars", "release_date": "2022-02-25", "price_range": "$5 - $9", "price_charting_link": "https://www.pricecharting.com/game/pokemon-brilliant-stars/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Astral Radiance", "release_date": "2022-05-27", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-astral-radiance/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Pokémon Go", "release_date": "2022-07-01", "price_range": "$4 - $8", "price_charting_link": "https://www.pricecharting.com/game/pokemon-go/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Lost Origin", "release_date": "2022-09-09", "price_range": "$7 - $12", "price_charting_link": "https://www.pricecharting.com/game/pokemon-lost-origin/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Silver Tempest", "release_date": "2022-11-11", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-silver-tempest/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Crown Zenith", "release_date": "2023-01-20", "price_range": "$6 - $10", "price_charting_link": "https://www.pricecharting.com/game/pokemon-crown-zenith/booster-pack"},

            # --- Scarlet & Violet Series ---
            {"tier": "Tier 4: Standard/Recent", "set_name": "Scarlet & Violet Base Set", "release_date": "2023-03-31", "price_range": "$3 - $5", "price_charting_link": "https://www.pricecharting.com/game/pokemon-scarlet-&-violet/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Paldea Evolved", "release_date": "2023-06-09", "price_range": "$4 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-paldea-evolved/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Obsidian Flames", "release_date": "2023-08-11", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-obsidian-flames/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Scarlet & Violet: 151", "release_date": "2023-09-22", "price_range": "$7 - $12", "price_charting_link": "https://www.pricecharting.com/game/pokemon-scarlet-&-violet-151/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Paradox Rift", "release_date": "2023-11-03", "price_range": "$4 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-paradox-rift/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Paldean Fates", "release_date": "2024-01-26", "price_range": "$5 - $8", "price_charting_link": "https://www.pricecharting.com/game/pokemon-paldean-fates/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Temporal Forces", "release_date": "2024-03-22", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-temporal-forces/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Twilight Masquerade", "release_date": "2024-05-24", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-twilight-masquerade/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Shrouded Fable", "release_date": "2024-08-02", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-shrouded-fable/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Stellar Crown", "release_date": "2024-09-13", "price_range": "$4 - $6", "price_charting_link": "https://www.pricecharting.com/game/pokemon-stellar-crown/booster-pack"},
            {"tier": "Tier 2: High-Value Modern", "set_name": "Surging Sparks", "release_date": "2024-11-08", "price_range": "$6 - $10", "price_charting_link": "https://www.pricecharting.com/game/pokemon-surging-sparks/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Prismatic Evolutions", "release_date": "2025-01-17", "price_range": "$8 - $12", "price_charting_link": "https://www.pricecharting.com/game/pokemon-prismatic-evolutions/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Journey Together", "release_date": "2025-03-28", "price_range": "$5 - $7", "price_charting_link": "https://www.pricecharting.com/game/pokemon-journey-together/booster-pack"},
            {"tier": "Tier 3: Popular & Strong", "set_name": "Destined Rivals", "release_date": "2025-05-01", "price_range": "$6 - $8", "price_charting_link": "https://www.pricecharting.com/game/pokemon-destined-rivals/booster-pack"},
            {"tier": "Tier 4: Standard/Recent", "set_name": "Scarlet & Violet: Black Bolt", "release_date": "2025-07-18", "price_range": "", "price_charting_link": ""}, # Upcoming, placeholder price
            {"tier": "Tier 4: Standard/Recent", "set_name": "Scarlet & Violet: White Flare", "release_date": "2025-07-18", "price_range": "", "price_charting_link": ""}, # Upcoming, placeholder price

            # --- Special Sets (not part of main series, but often have boosters) ---
            # Legendary Collection is a reprint set from Wizards of the Coast era.
            {"tier": "Tier 1: Ultra-Rare Vintage", "set_name": "Legendary Collection", "release_date": "2002-10-21", "price_range": "$500 - $1,500", "price_charting_link": "https://www.pricecharting.com/game/pokemon-legendary-collection/booster-pack"},
        ]

        for data in pack_data:
            data['release_date'] = datetime.datetime.strptime(data['release_date'], '%Y-%m-%d').date()
            BoosterPack.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added: {data["set_name"]}'))

        self.stdout.write(self.style.SUCCESS('Data loading complete!'))
