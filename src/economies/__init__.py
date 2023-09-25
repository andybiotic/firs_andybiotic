registered_economies = []

# specify economies in the order that they should appear in parameter list in-game (and also in docs)
# economies have a numeric ID which maps parameter values and avoids breaking savegames when this list changes
# !! ^ that doesn't appear to work, action 14 param doesn't seem to be able to abstract name value from name orde??

from economies import plains_trains_and_steel
from economies import black_gold_and_fire
from economies import trade_and_waves

plains_trains_and_steel.economy.register()
black_gold_and_fire.economy.register()
trade_and_waves.economy.register()
