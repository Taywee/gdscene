# WIP WARNING

This is currently not even useable.  This warning will disappear when the
project hits 1.0 (which should be relatively early.  I'll 1.0 it when it is even
minimally generally useable).  From 1.0 on, this will follow semantic
versioning.

# gdscene
Python module to ease automatic generation of Godot Scenes.  This is intended to
be used to easily export scene files that are programmatically generated, not to
import or parse scene files at all.  That may be added at some point, but it
likely will not, due to the complexity of parsing that would necessitate a
full-featured parser.

Note that this is not perfect, and there is a lot of magic that godot does that
this can not do yet, like generating imports.  You will probably need to make a
scene file manually, and use information from this to complete your program (or
to make your program work), and then generate the final scene over it.

# Use

Coming soon. Eventually, the use should look something like this, if the
intention is to split apart an image into some sort of tilemap:

```python
from gdscene require GdScene, ExtResource, SubResource, Node, Vector2, Rect2

# Things like Vector2 and Rect2 are convenience classes.  Almost all classes are
# printed by __repr__, with a few exceptions (like booleans), so Vector2 could
# be implemented like this (and indeed largely is, in these sources):
#
#   class Vector2:   
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#
#       def __repr__(self):
#           return f'Vector2( {self.x}, {self.y} )'
#
# This makes it incredibly easy to extend with your own types.  You can also use
# this to create some sort of literalstring class, like this:
#
#   class Literal:   
#       def __init__(self, value):
#           self.value = value
#
#       def __repr__(self):
#           return self.value
#
# So that you could directly represent the type as a string, so Literal('Vector2 (0, 0)')
# Would just return that string without quotes.


scene = GdScene(load_steps=8, format=2)

ext_resource = ExtResource(path="res://art/00.png")
stream_texture = SubResource(type='StreamTexture', flags=0, load_path="res://.import/00.png-10abfec7bb5e960ed10fdc1645014266.stex")
ext_resource.add(stream_texture)
rectangle_shape = SubResource(type='RectangleShape2d', custom_solver_bias=0.0, extents=Vector2(16, 16))
ext_resource.add(rectangle_shape)

tile_size = 32
width = 10
height = 11

root = Node(name="Root", type="node")

for y in range(height):
    for x in range(width):
        tileno = y * width + x
        sprite = Node(name=f"sprite{tileno}", type="Sprite")
        sprite['position'] = Vector2(x * tile_size, y * tile_size)
        sprite['texture'] = stream_texture
        sprite['region_enabled'] = True
        sprite['region_rect'] = Rect2(x * tile_size, y * tile_size, tile_size, tile_size)

        # Can be shortened to a convenience method:
        # body = sprite.add_node(name="StaticBody2D", type="StaticBody2D")
        body = Node(name="StaticBody2D", type="StaticBody2D")
        body['visible'] = False
        # etc etc
        sprite.add(body)

        shape = body.add_node(name="CollisionShape2D", type="CollisionShape2D")
        shape['shape'] = rectangle_shape

        root.add(sprite)

print(scene)
```

Aspects like "parent", "index" and "id" will be auto-created.

It's not exactly "easy", and involves a lot of necessary knowledge into the way
scenes work and the resources are arranged, but it is far easier than
hand-building these things, and is much better than trying to do it either by
hand or with some horrible vim macros.  The ideal is that this will be
eventually powerful enough to do a whole lot of gruntwork for you, but at the
very least, it'll make it easier to do things like generate tilemap scenes or
other highly-repetitive scenes easily.  Perhaps it might even make it easier to
write conversion tools to read some other format in and output it as a Godot
scene.

# Install

```sh
pip install gdscene
```

# License
GPL3
