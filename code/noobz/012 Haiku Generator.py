from random import choice

fives = "over the wintry", "with no leaves to blow", "an old silent pond", \
		"to see in this shell", "see only a hat", "the sound of water", \
		"Blowing from the west", "on the dirt road", "sunlight mixed with dust" \

sevens = "up to love porridge later", "love is a sweet summer rain", \
		"new colors glance in my hair", "as waves break over the bow", \
		 "from a colorful flower", "hurting everything it hits"

print("\n{},\n{},\n{}".format(choice(fives), choice(sevens), choice(fives)))