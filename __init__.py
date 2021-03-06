# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "Save Preferences from TopBar",
    "description": "Save Preferences button for TopBar",
    "author": "Daniel Grauer",
    "version": (1, 0, 4),
    "blender": (2, 82, 0),
    "location": "TopBar",
    "category": "System",
    "wiki_url": "https://github.com/kromar/blender_save_preferences_button"
}


def draw_button(self, context):
    if context.region.alignment == 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)
        row.operator(operator="screen.userpref_show", text="", icon='PREFERENCES', emboss=True)
        row.operator(operator="wm.save_userpref", text="", icon='IMPORT', emboss=True)
        row = layout.row(align=True)
        row.operator(operator="wm.save_homefile", text="", icon='FILE_BACKUP', emboss=True)
        row = layout.row(align=True)
        row.operator(operator="script.reload", text="", icon='FILE_SCRIPT', emboss=True)

        #bpy.ops.script.reload()


def register():
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)


def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)


if __name__ == "__main__":
    register()
